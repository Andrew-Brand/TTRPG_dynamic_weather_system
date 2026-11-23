"""Runs the weather model over a number of steps."""

import pandas as pd

from weather_model import config
from weather_model.generator import WeatherGenerator
from weather_model.navigator import Navigator
from weather_model.state import StateRange
from weather_model.tables import WeatherTables, load_tables


class Simulation:
    def __init__(self, tables: WeatherTables = None, state_range: StateRange = None):
        self.tables = tables or load_tables()
        self.state_range = state_range or StateRange()
        self.generator = WeatherGenerator(self.tables.states, self.state_range)
        self.navigator = Navigator(self.state_range)

    def run(self, runs: int = config.DEFAULT_RUNS, verbose: bool = False) -> pd.DataFrame:
        """Walk the model for `runs` steps and return the visited states.

        Returns a DataFrame with columns: run, humidity, temperature.
        """
        state = self.generator.random_start_state()
        print(f"{state.humidity}, {state.temperature} - {self.generator.get_weather(state)}")

        records = []
        for i in range(runs):
            records.append({"run": i, "humidity": state.humidity, "temperature": state.temperature})
            state = self.navigator.change_state(state)
            if verbose:
                print(f"{state.humidity}, {state.temperature} - {self.generator.get_weather(state)}")

        return pd.DataFrame(records, columns=["run", "humidity", "temperature"])
