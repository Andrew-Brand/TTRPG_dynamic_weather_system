import pandas as pd
import random as rnd
import os
from weather_model.set_state_ranges import set_state_range as ssr

def open_csv(name:str):
    script_dir = os.getcwd()
    full_path = os.path.join(script_dir, r'tables', name)
    return pd.read_csv(full_path, header=None)

def import_tables():
    pressure_humidity = open_csv('pressure-humidity.csv')
    wind = open_csv('wind_speeds.csv')
    states = open_csv('states.csv')
    return pressure_humidity, wind, states

def run(days:int, season:str, climate:str, humidity:str):
    p_h, wind, states = import_tables()

    state_range, range_centre = ssr()

    maxHumidity = state_range['humidity_high']
    minHumidity = state_range['humidity_low']
    maxTemp = state_range['temp_high']
    minTemp = state_range['temp_low']

    humidity = rnd.randrange(minHumidity, maxHumidity)
    temp = rnd.randrange(minTemp,maxTemp)

    weather = states.iloc[humidity, temp]

    return states, weather, temp, humidity, range_centre, maxTemp, maxHumidity