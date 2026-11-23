"""Loading of the CSV lookup tables."""

from dataclasses import dataclass

import pandas as pd

from weather_model import config


@dataclass
class WeatherTables:
    pressure_humidity: pd.DataFrame
    wind: pd.DataFrame
    states: pd.DataFrame


def open_csv(name: str) -> pd.DataFrame:
    """Read a headerless CSV from the tables directory."""
    return pd.read_csv(config.TABLES_DIR / name, header=None)


def load_tables() -> WeatherTables:
    return WeatherTables(
        pressure_humidity=open_csv(config.PRESSURE_HUMIDITY_CSV),
        wind=open_csv(config.WIND_SPEEDS_CSV),
        states=open_csv(config.STATES_CSV),
    )
