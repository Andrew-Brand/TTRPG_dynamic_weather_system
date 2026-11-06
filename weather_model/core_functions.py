from weather_model.weather import run
import weather_model.navigator as nav

def get_inputs():
    days = 1
    season = "test"
    climate = "test"
    humidity = "test"
    return days, season, climate, humidity

def main():
    days, season, climate, humidity = get_inputs()
    states, weather, temp, humidity, range_centre, maxTemp, maxHumidity = run(days, season, climate, humidity)
    print(f"{humidity}, {temp} - {weather}")
    newTemp, newIntensity = nav.change_state(temp, humidity, maxTemp, maxHumidity, range_centre)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity, maxTemp, maxHumidity, range_centre)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity, maxTemp, maxHumidity, range_centre)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity, maxTemp, maxHumidity, range_centre)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity, maxTemp, maxHumidity, range_centre)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity, maxTemp, maxHumidity, range_centre)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    return
