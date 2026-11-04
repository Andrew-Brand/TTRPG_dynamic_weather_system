import pandas as pd
import random as rnd

def import_tables():
    """import csv input tables from 'tables' directory"""
    p_h = pd.read_csv(r'tables\pressure-humidity.csv')
    wind = pd.read_csv(r'tables\wind_speeds.csv')
    states = pd.read_csv(r'tables\states.csv', header = None)
    return p_h, wind, states


def run(d:int, s:str, t:str, h:str):
    p_h, wind, states = import_tables()

    temp = rnd.randrange(1,11)
    intensity = rnd.randrange(1,8)

    weather = states.iloc[intensity,temp]

    return states, weather, temp, intensity

states, w, t, i = run(1,1,1,1)
