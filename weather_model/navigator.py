from random import randrange
import numpy as np

def change_state(temperature:int, intensity:int, maxTemp:int, maxIntensity:int):
    """ Shifts the weather state according to a probabilistic tendency towards a central """

    current_state = np.array([temperature, intensity])

    move = randrange(1,100)
    if 1 <= move <= 10:
        step = [0,0] # Stay in place
    elif 11 <= move <= 18:
        step = [0,1] # Move up
    elif 19 <= move <= 24:
        step = [1,1] # Move right and up
    elif 25 <= move <= 34:
        step = [1,0] # Move right
    elif 35 <= move <= 49:
        step = [1,-1] # Move right and down
    elif 50 <= move <= 69: #nice
        step = [0,-1] # Move down
    elif 69 <= move <=84:
        step = [-1,-1] # Move left and down
    elif 85 <= move <= 94:
        step = [-1,0] # Move left
    elif 95 <= move <= 100:
        step = [-1,1] # Move left and up
    else:
        step = [0,0] # Stay in place

    current_state = current_state + step

    temperature = current_state[0]
    temperature = min(temperature, maxTemp)
    temperature = max(temperature, 0)
    intensity = current_state[1]
    intensity = min(intensity, maxIntensity)
    intensity = max(intensity, 0)

    return temperature, intensity