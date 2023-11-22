import requests

def get_weather(api_key, city, country_code=''):    
    # Define the base URL for the OpenWeatherMap API
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    # Set the parameters for the API request
    params = {
        'q': f'{city},{country_code}',
        'appid': api_key,
        'units': 'imperial'  # You can change this to 'metric' for Celsius
    }

    # Make the API request using the 'requests' library
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()
        return weather_data
    else:
        # Print an error message if the request was not successful
        print(f"Error {response.status_code}: {response.text}")
        return None

def display_weather(weather_data):
    # Check if weather data is available
    if weather_data:
        # Extract relevant information from the weather data
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        # Display the weather information
        print(f"Weather: {main_weather} ({description})")
        print(f"Temperature: {temperature}°F")  # Displaying temperature in Fahrenheit
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        # Print a message if weather data retrieval fails
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    # Get the OpenWeatherMap API key from the user
    api_key = 'adec8d3ec2d9ee881802e40b0d7fea07'  # Replace with your own API key
    city = input("Enter the city: ")
    country_code = input("Enter the country code (optional, press Enter to skip): ")

    # Get weather data using the provided information
    weather_data = get_weather(api_key, city, country_code)
    
    # Display the weather information
    display_weather(weather_data)
