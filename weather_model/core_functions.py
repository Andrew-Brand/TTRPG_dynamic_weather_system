import pandas as pd
import weather_model.navigator as nav
from weather_model.weather import get_state
from weather_model.weather import get_weather
from weather_model.get_inputs import import_tables
import plotly.express as px
import matplotlib.pyplot as plt

def main(runs:int):
    p_h, wind, states = import_tables()

    humidity, temperature, humidity_range, temperature_range, range_centre = get_state()

    #For statistical analysis of outputs
    trend = pd.DataFrame(columns = ["run","humidity","temperature"])

    weather = get_weather(humidity, temperature, states)
    print(f"{humidity}, {temperature} - {weather}")

    for i in range(runs):
        s = pd.Series({"run": i, "humidity":humidity, "temperature":temperature})
        trend = pd.concat([trend, s.to_frame().T],ignore_index=True)
        humidity, temperature = nav.change_state(humidity, temperature, humidity_range, temperature_range, range_centre)
        weather = get_weather(humidity, temperature, states)
        # print(f"{humidity}, {temperature} - {weather}")

    print(f'max temp: {max(trend['temperature'])}\n'
          f'min temp: {min(trend['temperature'])}\n'
          f'max humidity: {max(trend['humidity'])}\n'
          f'min humidity: {min(trend['humidity'])}')

    fig,ax = plt.subplots()
    hb = ax.hexbin(trend['temperature'], trend['humidity'],gridsize=(12,8),extent=(0,23,0,16))
    ax.set(xlim=(0,23), ylim=(0,16))
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Humidity")
    plt.colorbar(hb,ax=ax,label='Count')
    plt.show()
    return
