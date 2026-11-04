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