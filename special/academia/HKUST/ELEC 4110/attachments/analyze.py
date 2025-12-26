import numpy as np
from os import path
import pandas as pd

_MAPPING = {
    "midterm examination data.csv": (
        "midterm examination analysis.csv",
        "midterm examination analysis.svg",
    ),
    "midterm examination data (1).csv": (
        "midterm examination analysis (1).csv",
        "midterm examination analysis (1).svg",
    ),
}


def main() -> None:
    for input_path, (data_output_path, plot_output_path) in _MAPPING.items():
        if not path.exists(input_path):
            continue

        data = pd.read_csv(input_path, header=0)
        data_plot = data.plot.hist(bins=np.linspace(0, 100, 21))  # type: ignore
        data_plot.set_xticks(np.linspace(0, 100, 11))

        data.describe().to_csv(data_output_path)  # type: ignore
        data_plot.figure.savefig(plot_output_path)  # type: ignore


if __name__ == "__main__":
    main()
