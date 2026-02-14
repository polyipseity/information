"""
---
requirements: pip install beautifulsoup4>=4.12.0 numpy>=2.0.0 pillow>=10.3.0 pyperclip>=1.9.0
timestamp: 2025-07-14T09L07:57.990+08:00
---

Solve tiling puzzle by computing edge differences.
"""

from base64 import decodebytes
from collections import defaultdict
from collections.abc import Callable, Iterable, Iterator, Mapping
from contextlib import contextmanager
from hashlib import sha3_512
from io import BytesIO
from json import dump, load
from pathlib import Path
from types import NoneType
from typing import Literal, NewType, TypeGuard, TypeVar

import numpy as np
from bs4 import BeautifulSoup
from numpy import dtype, float64, floating, ndarray, newaxis, uint8
from PIL import Image
from pyperclip import copy, paste

_T = TypeVar("_T")

Color = NewType("Color", ndarray[tuple[Literal[3]], dtype[uint8]])
TilePart = ndarray[tuple[int, int, Literal[3]], dtype[uint8]]
Tile = NewType("Tile", TilePart)
Position = NewType("Position", tuple[int, int])
Size = NewType("Size", tuple[int, int])


class Puzzle:
    def __init__(
        self,
        diff_func: Callable[[TilePart, TilePart], floating],
    ) -> None:
        self.board = defaultdict[Position, Tile | None](NoneType)
        self.keys = dict[Position, int]()
        self.diff_func = diff_func

    def set_edge_color(self, size: Size, color: Color) -> None:
        colored_tile = Tile(color[newaxis, newaxis])
        for yy in range(-1, size[0] + 1):
            self.board[Position((yy, -1))] = self.board[Position((yy, size[1]))] = (
                colored_tile
            )
        for xx in range(-1, size[1] + 1):
            self.board[Position((-1, xx))] = self.board[Position((size[0], xx))] = (
                colored_tile
            )

    def calculate_diff(self, pos: Position, tile: Tile) -> floating:
        diff = float64()
        if (other_tile := self.board[Position((pos[0] - 1, pos[1]))]) is not None:
            diff += self.diff_func(tile[0, :], other_tile[-1, :])
        if (other_tile := self.board[Position((pos[0], pos[1] + 1))]) is not None:
            diff += self.diff_func(tile[:, -1], other_tile[:, 0])
        if (other_tile := self.board[Position((pos[0] + 1, pos[1]))]) is not None:
            diff += self.diff_func(tile[-1, :], other_tile[0, :])
        if (other_tile := self.board[Position((pos[0], pos[1] - 1))]) is not None:
            diff += self.diff_func(tile[:, 0], other_tile[:, -1])
        return diff

    def set_best_tile(self, pos: Position, tiles: Mapping[int, Tile]) -> int:
        diffs = {key: self.calculate_diff(pos, tile) for key, tile in tiles.items()}
        key, _ = min(diffs.items(), key=lambda item: item[1])
        self.board[pos] = tiles[key]
        self.keys[pos] = key
        return key


def is_two_element_tuple(val: tuple[_T, ...]) -> TypeGuard[tuple[_T, _T]]:
    return len(val) == 2


@contextmanager
def tile_cache(path: Path):
    with open(path, "r+t") as file:
        try:
            cache: dict[str, list[int]] = load(file)
            cache2 = dict[str, tuple[int, int]]()
            for key, val in cache.items():
                val2 = tuple(val)
                if is_two_element_tuple(val2):
                    cache2[key] = val2
        except Exception:
            cache2 = {}
        try:
            yield cache2
        finally:
            file.seek(0)
            dump(cache2, file)
            file.truncate()


def detect_edges(tiles: Iterable[Tile]) -> tuple[Size, Color]:
    edge_colors = defaultdict[tuple[int, int, int], list[int]](lambda: [0, 0, 0, 0])
    for tile in tiles:
        top_left = tuple(tile[0, 0])
        bottom_right = tuple(tile[-1, -1])
        if np.all(tile[0, :] == top_left):
            edge_colors[top_left][0] += 1
        if np.all(tile[:, -1] == bottom_right):
            edge_colors[bottom_right][1] += 1
        if np.all(tile[-1, :] == bottom_right):
            edge_colors[bottom_right][2] += 1
        if np.all(tile[:, 0] == top_left):
            edge_colors[top_left][3] += 1
    edge_color, edge_color_votes = max(
        edge_colors.items(), key=lambda item: sum(item[1])
    )
    return Size((edge_color_votes[1], edge_color_votes[0])), Color(np.array(edge_color))


def diff(left: TilePart, right: TilePart, p: float = 1) -> floating:
    return np.sum(np.abs(left.astype(int) - right) ** p) ** (1 / p)


def consider_next_position(puzzle: Puzzle) -> Iterator[Position]:
    actions: tuple[
        Callable[[Position], Position],
        Callable[[Position], Position],
        Callable[[Position], Position],
        Callable[[Position], Position],
    ] = (
        lambda pos: Position((pos[0] - 1, pos[1])),
        lambda pos: Position((pos[0], pos[1] + 1)),
        lambda pos: Position((pos[0] + 1, pos[1])),
        lambda pos: Position((pos[0], pos[1] - 1)),
    )
    action = 1
    current_pos = Position((0, 0))
    while puzzle.board[current_pos] is None:
        yield current_pos
        old_action = action
        while puzzle.board[(next_pos := actions[action](current_pos))] is not None:
            action = (action + 1) % len(actions)
            if action == old_action:
                break
        current_pos = next_pos


def hash_tile(tile: Tile) -> str:
    return sha3_512(tile.tobytes()).digest().hex()


def main():
    tiles_to_keep = int(input("tiles to keep (default 0): ") or 0)
    input("HTML (will read from clipboard)? ")
    html_text = paste()

    html = BeautifulSoup(html_text, "html.parser")
    tile_els = html.select("img")
    tiles = {
        int(str(tile_el["n"])): Tile(
            np.array(
                Image.open(
                    BytesIO(decodebytes(str(tile_el["src"]).split(",", 1)[-1].encode()))
                ).convert("HSV")
            )
        )
        for tile_el in tile_els
    }
    size, edge_color = detect_edges(tiles.values())

    orig_puzzle, puzzle = Puzzle(diff), Puzzle(diff)
    orig_puzzle.set_edge_color(size, edge_color)
    puzzle.set_edge_color(size, edge_color)

    for idx, tile_el in enumerate(tile_els):
        key = int(str(tile_el["n"]))
        pos = Position((idx // size[1], idx % size[1]))
        orig_puzzle.board[pos] = tiles[key]
        orig_puzzle.keys[pos] = key

    with tile_cache(Path("cache.json")) as cache:
        for key, tile in tuple(tiles.items()):
            hash = hash_tile(tile)
            if (pos := cache.get(hash)) is not None:
                pos = Position(pos)

                # puzzle.board[pos] = tile
                puzzle.keys[pos] = key

        tiles_kept = 0
        cur_tiles = tiles.copy()
        considered_pos = list[Position]()
        for pos in consider_next_position(puzzle):
            print(pos)
            considered_pos.append(pos)
            if (key := puzzle.keys.get(pos)) is not None:
                tiles_kept += 1

                puzzle.board[pos] = cur_tiles[key]
                del cur_tiles[key]
                continue
            if tiles_kept < tiles_to_keep:
                tiles_kept += 1

                tile = orig_puzzle.board[pos]
                assert tile is not None
                key = orig_puzzle.keys[pos]
                cache[hash_tile(tile)] = pos

                puzzle.board[pos] = tile
                puzzle.keys[pos] = key
                del cur_tiles[key]
                continue
            key = puzzle.set_best_tile(pos, cur_tiles)
            del cur_tiles[key]

    """
    for _ in range(1):
        tiles_kept = 0
        cur_tiles = tiles.copy()
        for pos in considered_pos:
            print(pos)
            if tiles_kept < tiles_to_keep:
                tiles_kept += 1
                del cur_tiles[puzzle.keys[pos]]
                continue
            key = puzzle.set_best_tile(pos, cur_tiles)
            del cur_tiles[key]
    """

    sequence = tuple(
        key for _, key in sorted(puzzle.keys.items(), key=lambda item: item[0])
    )
    print(sequence)
    copy(
        f"""(function (sequence) {{
  const puzzle = document.querySelector("#board");
  const images = Object.fromEntries([...puzzle.querySelectorAll("img")].map(img => [Number(img.getAttribute("n")), img]));
  for (const key of sequence) {{
     puzzle.appendChild(images[key]);
  }}
}})({list(sequence)})"""
    )


if __name__ == "__main__":
    main()
