from math import ceil

from pandas import read_csv  # type: ignore

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
        data_plot = data.plot.hist(  # type: ignore[reportUnknownMemberType, reportUnknownVariableType]
            bins=range(int(data.min().iloc[0]), ceil(data.max().iloc[0]) + 1)  # type: ignore[reportArgumentType]
        )

        data.describe().to_csv(data_output_path)
        data_plot.figure.savefig(plot_output_path)  # type: ignore[reportUnknownMemberType]


if __name__ == "__main__":
    main()
