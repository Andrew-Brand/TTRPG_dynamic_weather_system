import pandas as pd
import os

def open_csv(name:str):
    script_dir = os.getcwd()
    full_path = os.path.join(script_dir, r'tables', name)
    return pd.read_csv(full_path, header=None)

def import_tables():
    pressure_humidity = open_csv('pressure-humidity.csv')
    wind = open_csv('wind_speeds.csv')
    states = open_csv('states.csv')
    return pressure_humidity, wind, states

def user_inputs():
    days = 1
    season = "test"
    climate = "test"
    humidity = "test"
    return days, season, climate, humidity