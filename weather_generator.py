"""This is the main file to run when generating weather for this package.

See README.md for full details.

Required user inputs:
    - days          INT         The number of days to run weather model for.

    - season        STRING      The current season:
                                    - spring, summer, autumn, winter

    - temperature   STRING      The general temperature of the climate in a given region:
                                    - tropical, subtropical, temperate, subpolar, polar

    - humidity      STRING      The general humidity of the climate in a given region:
                                    - humid, subhumid, semiarid,arid,hyperarid
"""
from weather_model.weather import run

def get_inputs():
    days = int(input("Enter the number of days to run weather model for: "))
    season = input("Enter season: ")
    temperature = input("Enter region temperature: ")
    humidity = input("Enter region humidity: ")
    return days, season, temperature, humidity

def main():
    days, season, temperature, humidity = get_inputs()
    run(days, season, temperature, humidity)
    return


#Not sure why this is standard practice but I'll do it anyway!
if __name__ == "__main__":
    main()