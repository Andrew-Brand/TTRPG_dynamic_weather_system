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
    states, weather, temp, intensity = run(days, season, climate, humidity)
    maxTemp = states.shape[1] - 1
    maxIntensity = states.shape[0] - 1
    print(f"{intensity}, {temp} - {weather}")
    newTemp, newIntensity = nav.change_state(temp, intensity, maxTemp, maxIntensity)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity, maxTemp, maxIntensity)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity, maxTemp, maxIntensity)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity, maxTemp, maxIntensity)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity, maxTemp, maxIntensity)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity, maxTemp, maxIntensity)
    print(f"{newIntensity}, {newTemp} - {states.iloc[newIntensity, newTemp]}")
    return

main()
