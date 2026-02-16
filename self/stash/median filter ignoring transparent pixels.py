"""
---
requirements: pip install numpy>=2.0.0 opencv-python>=4.13.0
timestamp: 2025-04-14T10:24:02.074+08:00
---

Median filter ignoring transparent pixels. Maybe run this twice for better effect...?
"""

import argparse
from anyio import Path
import sys

import cv2
from os import PathLike
import numpy as np


DEFAULT_KSIZE = 3
DEFAULT_INPUT = "input.png"
DEFAULT_OUTPUT = "output.png"


def read_image(path: PathLike[str]) -> np.ndarray:
    """Read image with alpha preserved (IMREAD_UNCHANGED).

    Raises FileNotFoundError if the file cannot be read.
    """
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise FileNotFoundError(f"Could not read image: {path}")
    return img


def ensure_bgra(image: np.ndarray) -> np.ndarray:
    """Ensure image has 4 channels (BGRA) and dtype=uint8.

    - If grayscale (H,W) → convert to BGRA
    - If BGR (H,W,3) → add opaque alpha
    - If already BGRA, return a copy with correct dtype
    """
    if image.dtype != np.uint8:
        image = image.astype(np.uint8)

    if image.ndim == 2:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2BGRA)

    if image.shape[2] == 3:
        bgr = image
        alpha = np.full(bgr.shape[:2] + (1,), 255, dtype=np.uint8)
        return np.concatenate((bgr, alpha), axis=2)

    if image.shape[2] == 4:
        return image.copy()

    raise ValueError(f"Unsupported number of channels: {image.shape[2]}")


def compute_color_palette(
    image_flat: np.ndarray, *, min_count: int = 2048, special: np.typing.ArrayLike | None = None
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Compute color frequency palette (kept from original script).

    Returns (colors, counts, color_palette, color_palette_round).
    """
    if special is None:
        special = []

    colors, counts = np.unique(image_flat, return_counts=True)
    color_palette = colors[(counts >= min_count) | (np.isin(counts, special))]
    color_palette_round = colors[~((counts >= min_count) | (np.isin(counts, special)))]
    return colors, counts, color_palette, color_palette_round


def median_filter_ignoring_transparent(image: np.ndarray, k_size: int) -> np.ndarray:
    """Perform the same median filter logic as the original script.

    - Treat 0 (uint32) as transparent and ignore it when computing local medians.
    - Preserves the original algorithm and comments.
    """
    # original shape (H, W, 4)
    shape = image.shape

    # Flatten to uint32 per-pixel value (BGRA packed into uint32)
    image_flat = image.reshape(-1).view(np.uint32).reshape(shape[:-1])

    # --- preserved color-palette computation (unused by default) ---
    _colors, _counts, _color_palette, _color_palette_round = compute_color_palette(
        image_flat
    )  # intentionally unused (kept for reference)

    # ----
    # Keep the original commented mapping block in-place for readability / future use
    """
    mapping = np.argmin(
        np.sum(
            (
                color_palette.view(np.uint8).reshape((-1, 4))
                - color_palette_round.view(np.uint8).reshape((-1, 1, 4))
            )
            ** 2,
            axis=-1,
        ),
        axis=-1,
    )
    for idx, a in enumerate(color_palette_round):
        image_flat[image_flat == a] = 0
    """
    # ---------------------------------------------------------------

    if k_size % 2 == 0 or k_size < 1:
        raise ValueError("k_size must be a positive odd integer")

    # use integer buffers (avoid unnecessary float upcasts)
    new_image = np.empty(shape[:-1] + (k_size**2,), dtype=np.uint32)
    image_pad = (
        cv2.copyMakeBorder(
            image_flat.view(np.uint8).reshape(shape),
            k_size // 2,
            k_size // 2,
            k_size // 2,
            k_size // 2,
            borderType=cv2.BORDER_REPLICATE,
        )
        .view(np.uint32)
        .reshape(np.array(shape[:-1]) + np.array([k_size // 2 * 2, k_size // 2 * 2]))
    )

    new_image_min = np.zeros(shape[:-1], dtype=np.uint32)
    for idx in range(k_size**2):
        x = idx % k_size
        y = idx // k_size
        section = image_pad[y:, x:][: shape[0], : shape[1]]
        new_image[..., idx] = section
        new_image_min[
            ((new_image_min == 0) | (new_image_min > section)) & (section != 0)
        ] = section[((new_image_min == 0) | (new_image_min > section)) & (section != 0)]

    new_image_mask = new_image < new_image_min[..., np.newaxis]
    new_image = (1 - new_image_mask) * new_image + new_image_mask * new_image_min[
        ..., np.newaxis
    ]
    new_image = np.median(new_image, axis=-1).astype(np.uint32)

    # image_flat = cv2.medianBlur(image_flat, 3)
    image_flat[image_flat == 0] = new_image[image_flat == 0]

    # Reconstruct BGRA image from packed uint32 view
    out_image = image_flat.view(np.uint8).reshape(shape)
    return out_image


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Median filter that ignores transparent pixels"
    )
    p.add_argument("input", nargs="?", default=DEFAULT_INPUT, help="input image path")
    p.add_argument(
        "output", nargs="?", default=DEFAULT_OUTPUT, help="output image path"
    )
    p.add_argument(
        "-k",
        "--ksize",
        type=int,
        default=DEFAULT_KSIZE,
        help="kernel size (odd integer)",
    )
    p.add_argument(
        "--repeat", type=int, default=1, help="how many passes to run (default: 1)"
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    in_path = Path(args.input)
    out_path = Path(args.output)

    if args.ksize % 2 == 0 or args.ksize < 1:
        print("--ksize must be a positive odd integer", file=sys.stderr)
        return 2

    try:
        img = read_image(in_path)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 1

    # Ensure we have 4 channels (BGRA) so packing into uint32 is stable
    img = ensure_bgra(img)

    result = img
    for _ in range(max(1, int(args.repeat))):
        result = median_filter_ignoring_transparent(result, args.ksize)

    # ---------------------------------------------------------------
    # Preserve the original commented-out morphology example
    """
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel=np.array([
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1],
    ]))
    """
    # ---------------------------------------------------------------

    ok = cv2.imwrite(str(out_path), result)
    if not ok:
        print(f"Failed to write output image: {out_path}", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    exit(main())
