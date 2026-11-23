"""This is the main file to run when generating weather for this package.

See README.md for full details.

Required user inputs:
    - days          INT         The number of days to run weather model for.

    - season        STRING      The current season:
                                    - spring, summer, autumn, winter

    - climate       STRING      The general climate in a given region:
                                    - tropical, subtropical, temperate, subpolar, polar

    - humidity      STRING      The general humidity of the climate in a given region:
                                    - humid, subhumid, semiarid,arid,hyperarid
"""

from weather_model import config
from weather_model.reporting import plot_hexbin, print_summary
from weather_model.simulation import Simulation


def main(runs: int = config.DEFAULT_RUNS) -> None:
    trend = Simulation().run(runs)
    print_summary(trend)
    plot_hexbin(trend)


if __name__ == "__main__":
    main()
