"""Weather lookup and initial-state selection."""

import random as rnd

import pandas as pd

from weather_model.state import StateRange, WeatherState


class WeatherGenerator:
    """Maps grid states to weather descriptions."""

    def __init__(self, states: pd.DataFrame, state_range: StateRange):
        self.states = states
        self.state_range = state_range

    def get_weather(self, state: WeatherState) -> str:
        return self.states.iloc[state.humidity, state.temperature]

    def random_start_state(self) -> WeatherState:
        r = self.state_range
        # Draw order (humidity, then temperature) is kept so seeded runs are reproducible.
        humidity = rnd.randrange(r.humidity_low, r.humidity_high)
        temperature = rnd.randrange(r.temperature_low, r.temperature_high)
        return WeatherState(humidity, temperature)
