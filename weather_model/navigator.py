from random import randrange
import numpy as np

def change_state(humidity:int, temperature:int, maxTemp:int, maxHumidity:int,range_centre:list):
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

    if humidity < range_centre[0]:
        steps_dict['up_left'] -=4
        steps_dict['up'] -=5
        steps_dict['up_right'] -= 4
        steps_dict['down_right'] +=4
        steps_dict['down'] += 5
        steps_dict['down_left'] +=4
    elif humidity > range_centre[0]:
        steps_dict['up_left'] += 4
        steps_dict['up'] += 5
        steps_dict['up_right'] += 4
        steps_dict['down_right'] -= 4
        steps_dict['down'] -= 5
        steps_dict['down_left'] -= 4
    else:
        pass

    if temperature < range_centre[1]:
        steps_dict['up_right'] +=4
        steps_dict['right'] +=5
        steps_dict['down_right'] += 4
        steps_dict['up_left'] -=4
        steps_dict['left'] -= 5
        steps_dict['down_left'] -=4
    elif temperature > range_centre[1]:
        steps_dict['up_right'] -=4
        steps_dict['right'] -=5
        steps_dict['down_right'] -= 4
        steps_dict['up_left'] +=4
        steps_dict['left'] += 5
        steps_dict['down_left'] +=4
    else:
        pass

    move = randrange(1,100)
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
    humidity = min(humidity, maxHumidity)
    humidity = max(humidity, 0)
    temperature = current_state[1]
    temperature = min(temperature, maxTemp)
    temperature = max(temperature, 1)

    return humidity, temperature