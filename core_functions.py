from weather_model.weather import run
import weather_model.navigator as nav

def get_inputs():
    days = int(input("Enter the number of days to run weather model for: "))
    season = input("Enter season: ")
    climate = input("Enter region climate: ")
    humidity = input("Enter region humidity: ")
    return days, season, climate, humidity

def main():
    days, season, climate, humidity = get_inputs()
    states, weather, temp, intensity = run(days, season, climate, humidity)
    print(f"{temp}, {intensity} - {weather}")
    newTemp, newIntensity = nav.change_state(temp, intensity)
    print(f"{newTemp}, {newIntensity} - {states.iloc[newTemp, newIntensity]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity)
    print(f"{newTemp}, {newIntensity} - {states.iloc[newTemp, newIntensity]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity)
    print(f"{newTemp}, {newIntensity} - {states.iloc[newTemp, newIntensity]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity)
    print(f"{newTemp}, {newIntensity} - {states.iloc[newTemp, newIntensity]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity)
    print(f"{newTemp}, {newIntensity} - {states.iloc[newTemp, newIntensity]}")
    newTemp, newIntensity = nav.change_state(newTemp, newIntensity)
    print(f"{newTemp}, {newIntensity} - {states.iloc[newTemp, newIntensity]}")
    return

main()
