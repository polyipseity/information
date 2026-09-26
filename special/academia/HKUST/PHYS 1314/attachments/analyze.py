#!/usr/bin/env python
# /// script
# dependencies = [
#   "matplotlib>=3.11.0",
#   "pandas>=3.0.0",
# ]
# requires-python = ">=3.13.0"
# ///

from math import ceil

import matplotlib
from pandas import read_csv

# Reproducible SVG output. matplotlib salts the element ids it generates with a
# fresh uuid4 per process, so redrawing an unchanged histogram still produces a
# diff; pinning the salt makes a regenerated file byte-identical to the
# committed one. The date is dropped outright via ``metadata`` on the savefig
# call below. Changing the salt rewrites every SVG this script produces.
matplotlib.rcParams["svg.hashsalt"] = "information.academia-ingest"

_MAPPING = {
    "final examination data.csv": (
        "final examination analysis.csv",
        "final examination analysis.svg",
    ),
    "midterm examination data.csv": (
        "midterm examination analysis.csv",
        "midterm examination analysis.svg",
    ),
}


def main() -> None:
    for input_path, (data_output_path, plot_output_path) in _MAPPING.items():
        data = read_csv(input_path, header=0)
        data_plot = data.plot.hist(
            bins=range(int(data.min().iloc[0]), ceil(data.max().iloc[0]) + 1)
        )

        data.describe().to_csv(data_output_path)
        data_plot.figure.savefig(plot_output_path, metadata={"Date": None})


def __main__():
    main()


if __name__ == "__main__":
    __main__()
