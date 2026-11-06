"""This is the main file to run when generating weather for this package.

See README.md for full details.

Required user inputs:
    - days          INT         The number of days to run weather model for.

    - season        STRING      The current season:
                                    - spring, summer, autumn, winter

    - climate       STRING      The general climate in a given region:
                                    - tropical, subtropical, temperate, subpolar, polar

    - humidity      STRING      The general humidity of the climate in a given region:
                                    - humid, subhumid, semiarid,arid,hyperarid
"""

from weather_model.core_functions import main

#Not sure why this is standard practice, but I'm doing it anyway!
if __name__ == "__main__":
    main()