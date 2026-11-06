def set_state_range():
    """ Eventually will determine the upper and lower bounds of the temperature and humidity ranges for the states table"""

    state_range = {'humidity_low':0,
                   'humidity_high':16,
                   'temperature_low':0,
                   'temperature_high':23}

    range_centre = list([
        round((state_range['humidity_low']+state_range['humidity_high'])/2),
        round((state_range['temperature_low']+state_range['temperature_high'])/2)
    ])

    return state_range, range_centre