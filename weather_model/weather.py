import pandas as pd
import random as rnd
import os
from weather_model.set_state_ranges import set_state_range as ssr

def get_weather(humidity:int, temperature:int, states):
    weather = states.iloc[humidity, temperature]
    return weather

def get_state():
    state_range, range_centre = ssr()

    humidity_range = [state_range['humidity_low'],state_range['humidity_high']]
    temperature_range = [state_range['temperature_low'],state_range['temperature_high']]

    humidity = rnd.randrange(humidity_range[0], humidity_range[1])
    temperature = rnd.randrange(temperature_range[0],temperature_range[1])

    return humidity, temperature, humidity_range, temperature_range, range_centre