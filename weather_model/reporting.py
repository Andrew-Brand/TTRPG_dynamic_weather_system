"""Statistical summary and plotting of simulation output."""

import matplotlib.pyplot as plt
import pandas as pd

from weather_model import config
from weather_model.state import StateRange


def print_summary(trend: pd.DataFrame) -> None:
    print(
        f"max temp: {trend['temperature'].max()}\n"
        f"min temp: {trend['temperature'].min()}\n"
        f"max humidity: {trend['humidity'].max()}\n"
        f"min humidity: {trend['humidity'].min()}"
    )


def plot_hexbin(trend: pd.DataFrame, state_range: StateRange = None) -> None:
    r = state_range or StateRange()
    xlim = (r.temperature_low, r.temperature_high)
    ylim = (r.humidity_low, r.humidity_high)

    fig, ax = plt.subplots()
    hb = ax.hexbin(
        trend["temperature"], trend["humidity"],
        gridsize=config.HEXBIN_GRIDSIZE,
        extent=(*xlim, *ylim),
    )
    ax.set(xlim=xlim, ylim=ylim)
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Humidity")
    plt.colorbar(hb, ax=ax, label="Count")
    plt.show()
