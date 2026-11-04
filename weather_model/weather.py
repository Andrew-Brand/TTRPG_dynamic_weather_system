import pandas as pd
import random as rnd

def import_tables():
    """import csv input tables from 'tables' directory"""
    p_h = pd.read_csv(r'TTRPG_dynamic_weather_system/tables/pressure-humidity.csv')
    wind = pd.read_csv(r'TTRPG_dynamic_weather_system/tables/wind_speeds.csv')
    states = pd.read_csv(r'TTRPG_dynamic_weather_system/tables/states.csv', header = None)
    return p_h, wind, states

def run(d:int, s:str, t:str, h:str):
    p_h, wind, states = import_tables()

    cols = states.shape[1]
    rows = states.shape[0]

    intensity = rnd.randrange(0,rows)
    temp = rnd.randrange(0,cols)

    weather = states.iloc[intensity,temp]

    return states, weather, temp, intensity

states, w, t, i = run(1,1,1,1)
