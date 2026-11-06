import random as rnd
import numpy as np

def change_state(humidity:int, temperature:int, humidity_range:list, temperature_range:list, range_centre:list):
    """ Shifts the weather state according to a probabilistic tendency towards a central """

    current_state = np.array([humidity, temperature])
    steps_dict = {'stay':       12,
                  'up':         11,
                  'up_right':   11,
                  'right':      11,
                  'down_right': 11,
                  'down':       11,
                  'down_left':  11,
                  'left':       11,
                  'up_left':    11
                  }
    vert_pc_shift = 1.7
    horiz_pc_shift = 1.2

    if humidity < range_centre[0]:
        steps_dict['up_left'] -=vert_pc_shift
        steps_dict['up'] -=vert_pc_shift
        steps_dict['up_right'] -=vert_pc_shift
        steps_dict['down_right'] +=vert_pc_shift
        steps_dict['down'] +=vert_pc_shift
        steps_dict['down_left'] +=vert_pc_shift
    elif humidity > range_centre[0]:
        steps_dict['up_left'] +=vert_pc_shift
        steps_dict['up'] +=vert_pc_shift
        steps_dict['up_right'] +=vert_pc_shift
        steps_dict['down_right'] -=vert_pc_shift
        steps_dict['down'] -=vert_pc_shift
        steps_dict['down_left'] -=vert_pc_shift
    else:
        pass

    if temperature < range_centre[1]:
        steps_dict['up_right'] +=horiz_pc_shift
        steps_dict['right'] +=horiz_pc_shift
        steps_dict['down_right'] +=horiz_pc_shift
        steps_dict['up_left'] -=horiz_pc_shift
        steps_dict['left'] -=horiz_pc_shift
        steps_dict['down_left'] -=horiz_pc_shift
    elif temperature > range_centre[1]:
        steps_dict['up_right'] -=horiz_pc_shift
        steps_dict['right'] -=horiz_pc_shift
        steps_dict['down_right'] -=horiz_pc_shift
        steps_dict['up_left'] +=horiz_pc_shift
        steps_dict['left'] +=horiz_pc_shift
        steps_dict['down_left'] +=horiz_pc_shift
    else:
        pass

    move = round(rnd.uniform(1,100),1)
    if  move <= steps_dict['stay']:
        step = [0,0] # Stay in place
    elif move <= sum(list(steps_dict.values())[:2]):
        step = [-1,0] # Move up
    elif move <= sum(list(steps_dict.values())[:3]):
        step = [-1,1] # Move right and up
    elif move <= sum(list(steps_dict.values())[:4]):
        step = [0,1] # Move right
    elif move <= sum(list(steps_dict.values())[:5]):
        step = [1,1] # Move right and down
    elif move <= sum(list(steps_dict.values())[:6]):
        step = [1,0] # Move down
    elif move <=sum(list(steps_dict.values())[:7]):
        step = [1,-1] # Move left and down
    elif move <= sum(list(steps_dict.values())[:8]):
        step = [0,-1] # Move left
    elif move <= 100:
        step = [-1,-1] # Move left and up
    else:
        step = [0,0] # Stay in place

    current_state = current_state + step

    humidity = current_state[0]
    humidity = max(humidity, humidity_range[0])
    humidity = min(humidity, humidity_range[1])
    temperature = current_state[1]
    temperature = max(temperature, temperature_range[0])
    temperature = min(temperature, temperature_range[1])

    return humidity, temperature