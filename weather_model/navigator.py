from random import randrange
import numpy as np

def change_state(temperature:int, humidity:int, maxTemp:int, maxHumidity:int,range_centre:list):
    """ Shifts the weather state according to a probabilistic tendency towards a central """

    current_state = np.array([temperature, humidity])
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

    if humidity < range_centre[0]:
        steps_dict['up_left'] -=3
        steps_dict['up'] -=3
        steps_dict['up_right'] -= 3
        steps_dict['down_right'] +=3
        steps_dict['down'] += 3
        steps_dict['down_left'] +=3
    elif humidity > range_centre[0]:
        steps_dict['up_left'] += 3
        steps_dict['up'] += 3
        steps_dict['up_right'] += 3
        steps_dict['down_right'] -= 3
        steps_dict['down'] -= 3
        steps_dict['down_left'] -= 3
    else:
        pass

    if temperature < range_centre[1]:
        steps_dict['up_right'] +=3
        steps_dict['right'] +=3
        steps_dict['down_right'] += 3
        steps_dict['up_left'] -=3
        steps_dict['left'] -= 3
        steps_dict['down_left'] -=3
    elif temperature > range_centre[1]:
        steps_dict['up_right'] -=3
        steps_dict['right'] -=3
        steps_dict['down_right'] -= 3
        steps_dict['up_left'] +=3
        steps_dict['left'] += 3
        steps_dict['down_left'] +=3
    else:
        pass

    move = randrange(1,100)
    if  move <= steps_dict['stay']:
        step = [0,0] # Stay in place
    elif move <= sum(list(steps_dict.values())[:2]):
        step = [0,0]
        step = [0,1] # Move up
    elif move <= sum(list(steps_dict.values())[:3]):
        step = [1,1] # Move right and up
    elif move <= sum(list(steps_dict.values())[:4]):
        step = [1,0] # Move right
    elif move <= sum(list(steps_dict.values())[:5]):
        step = [1,-1] # Move right and down
    elif move <= sum(list(steps_dict.values())[:6]): #nice
        step = [0,-1] # Move down
    elif move <=sum(list(steps_dict.values())[:7]):
        step = [-1,-1] # Move left and down
    elif move <= sum(list(steps_dict.values())[:8]):
        step = [-1,0] # Move left
    elif move <= 100:
        step = [-1,1] # Move left and up
    else:
        step = [0,0] # Stay in place

    current_state = current_state + step

    temperature = current_state[0]
    temperature = min(temperature, maxTemp)
    temperature = max(temperature, 0)
    humidity = current_state[1]
    humidity = min(humidity, maxHumidity)
    humidity = max(humidity, 0)

    return temperature, humidity