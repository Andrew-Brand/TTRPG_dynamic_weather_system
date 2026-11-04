from random import randrange
import numpy as np

def change_state(temperature, intensity):
    """ Shifts the weather state according to a probabilistic tendency towards a central """

    current_state = np.array([temperature, intensity])

    moves_dict = {
        1: [0,0],
        2: [0,1],
        3: [1,1],
        4: [1,0],
        5: [1,-1],
        6: [0,-1],
        7: [-1,-1],
        8: [-1,0],
        9: [-1,1],
    }

    move = moves_dict[randrange(1,9)]

    current_state = current_state + move

    temperature = current_state[0]
    intensity = current_state[1]

    return temperature, intensity

temperature = 1
intensity = 1