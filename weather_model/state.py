"""Value types describing a position on the weather grid."""

from dataclasses import dataclass

from weather_model import config


@dataclass(frozen=True)
class WeatherState:
    """A cell on the states table (row = humidity, column = temperature)."""
    humidity: int
    temperature: int


@dataclass(frozen=True)
class StateRange:
    """Inclusive bounds of the humidity and temperature indices.

    Eventually these will be derived from the region's climate inputs.
    """
    humidity_low: int = config.HUMIDITY_LOW
    humidity_high: int = config.HUMIDITY_HIGH
    temperature_low: int = config.TEMPERATURE_LOW
    temperature_high: int = config.TEMPERATURE_HIGH

    @property
    def centre(self) -> WeatherState:
        return WeatherState(
            humidity=round((self.humidity_low + self.humidity_high) / 2),
            temperature=round((self.temperature_low + self.temperature_high) / 2),
        )

    def clamp(self, humidity: int, temperature: int) -> WeatherState:
        return WeatherState(
            humidity=min(max(humidity, self.humidity_low), self.humidity_high),
            temperature=min(max(temperature, self.temperature_low), self.temperature_high),
        )
