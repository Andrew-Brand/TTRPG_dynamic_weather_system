import pandas as pd
import random as rnd
import os

def open_csv(name:str):
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, 'tables', name)
    return pd.read_csv(full_path)

def import_tables():
    pressure_humidity = open_csv("pressure-humidity.csv")
    wind = open_csv('wind_speeds.csv')
    states = open_csv('states.csv')
    return pressure_humidity, wind, states

def run(days:int, season:str, climate:str, humidity:str):
    p_h, wind, states = import_tables()

    cols = states.shape[1]
    rows = states.shape[0]

    intensity = rnd.randrange(0,rows)
    temp = rnd.randrange(0,cols)

    weather = states.iloc[intensity,temp]

    return states, weather, temp, intensity

states, w, t, i = run(1,"1","1","1")
