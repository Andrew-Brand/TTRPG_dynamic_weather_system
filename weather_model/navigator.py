from random import randrange
import numpy as np

def change_state(temperature, intensity):
    """ Shifts the weather state according to a probabilistic tendency towards a central """

    current_state = np.array([temperature, intensity])

    move = randrange(1,100)
    if 1 <= move <= 10:
        step = [0,0]
    elif 11 <= move <= 18:
        step = [0,1]
    elif 19 <= move <= 24:
        step = [1,1]
    elif 25 <= move <= 34:
        step = [1,0]
    elif 35 <= move <= 49:
        step = [1,-1]
    elif 50 <= move <= 69: #nice
        step = [0,-1]
    elif 69 <= move <=84:
        step = [-1,-1]
    elif 85 <= move <= 94:
        step = [-1,0]
    elif 95 <= move <= 100:
        step = [-1,1]
    else:
        step = [0,0]

    current_state = current_state + step

    temperature = current_state[0]
    intensity = current_state[1]

    return temperature, intensity