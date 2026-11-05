def set_state_range():
    """ Eventually will determine the upper and lower bounds of the temperature and humidity ranges for the states table"""

    state_range = {'temp_low':4,
                  'temp_high':16,
                  'humidity_low':0,
                  'humidity_high':15}

    range_centre = list([
        round((state_range['humidity_low']+state_range['humidity_high'])/2),
        round((state_range['temp_low']+state_range['temp_high'])/2)
    ])

    return state_range, range_centre