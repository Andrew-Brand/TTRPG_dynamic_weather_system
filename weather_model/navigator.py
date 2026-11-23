"""Probabilistic movement of the weather state across the grid."""

import random as rnd

from weather_model import config
from weather_model.state import StateRange, WeatherState


class Navigator:
    """Shifts the weather state with a probabilistic tendency towards the centre."""

    def __init__(
        self,
        state_range: StateRange,
        vert_pc_shift: float = config.VERTICAL_PC_SHIFT,
        horiz_pc_shift: float = config.HORIZONTAL_PC_SHIFT,
    ):
        self.state_range = state_range
        self.centre = state_range.centre
        self.vert_pc_shift = vert_pc_shift
        self.horiz_pc_shift = horiz_pc_shift

    def _step_weights(self, state: WeatherState) -> dict:
        """Base step weights, biased towards the centre of the grid."""
        weights = dict(config.BASE_STEP_WEIGHTS)
        v, h = self.vert_pc_shift, self.horiz_pc_shift

        if state.humidity < self.centre.humidity:
            for k in ("up_left", "up", "up_right"):
                weights[k] -= v
            for k in ("down_right", "down", "down_left"):
                weights[k] += v
        elif state.humidity > self.centre.humidity:
            for k in ("up_left", "up", "up_right"):
                weights[k] += v
            for k in ("down_right", "down", "down_left"):
                weights[k] -= v

        if state.temperature < self.centre.temperature:
            for k in ("up_right", "right", "down_right"):
                weights[k] += h
            for k in ("up_left", "left", "down_left"):
                weights[k] -= h
        elif state.temperature > self.centre.temperature:
            for k in ("up_right", "right", "down_right"):
                weights[k] -= h
            for k in ("up_left", "left", "down_left"):
                weights[k] += h

        return weights

    @staticmethod
    def _pick_step(weights: dict) -> tuple:
        """Roll 1-100 and map it onto the cumulative step weights."""
        move = round(rnd.uniform(1, 100), 1)
        names = list(config.STEP_DELTAS)
        values = [weights[n] for n in names]

        for i, name in enumerate(names[:-1], start=1):
            if move <= sum(values[:i]):
                return config.STEP_DELTAS[name]
        if move <= 100:
            return config.STEP_DELTAS[names[-1]]
        return config.STEP_DELTAS["stay"]

    def change_state(self, state: WeatherState) -> WeatherState:
        d_humidity, d_temperature = self._pick_step(self._step_weights(state))
        return self.state_range.clamp(
            state.humidity + d_humidity,
            state.temperature + d_temperature,
        )
