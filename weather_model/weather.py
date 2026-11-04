import pandas as pd

def import_tables():
    """import csv input tables from 'tables' directory"""
    p_h = pd.read_csv(f'tables\pressure-humidity.csv')
    wind = pd.read_csv(f'tables\wind_speeds.csv')
    states = pd.read_csv(f'tables\states.csv')
    return p_h, wind, states


def run(d:int, s:str, t:str, h:str):
    p_h, wind, states = import_tables()
    return print("test")