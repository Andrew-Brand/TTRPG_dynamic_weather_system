import pandas as pd
import random as rnd
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

def run(days:int, season:str, climate:str, humidity:str):
    p_h, wind, states = import_tables()

    maxIntensity = states.shape[0] - 1
    maxTemperature = states.shape[1] - 1

    temp = rnd.randrange(0,maxTemperature)
    intensity = rnd.randrange(0,maxIntensity)

    weather = states.iloc[intensity, temp]

    return states, weather, temp, intensity
