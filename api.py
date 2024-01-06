""" Kunsang Tsering """

def get_weather():
    # Function to retrieve weather information for New York
    Base_URL = "                                              "
    API_KEY = "                                               "
    CITY = "New York"

    # Function to convert temperature from Kelvin to Celsius and Fahrenheit
    def kt_to_celsius_fahrenheit(kt):
        celsius = kt - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

    # Constructing the URL with parameters (city and API key)
    url = f"{Base_URL}?q={CITY}&appid={API_KEY}"

    # Sending a GET request to the OpenWeatherMap API and converting the response to JSON
    response = requests.get(url).json()

    # Extracting weather information from the API response
    temperature_kt = response['main']['temp']
    celsius, fahrenheit = kt_to_celsius_fahrenheit(temperature_kt)

    sunrise_time = dt.datetime.utcfromtimestamp(
        response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(
        response['sys']['sunset'] + response['timezone'])

    formatted_sunrise_time = sunrise_time.strftime("%I:%M %p")
    formatted_sunset_time = sunset_time.strftime("%I:%M %p")

    # Returning a dictionary containing weather information
    return {
        "Temperature in Celsius": celsius,
        "Temperature in Fahrenheit": fahrenheit,
        "Sunrise Time": formatted_sunrise_time,
        "Sunset Time": formatted_sunset_time
    }
