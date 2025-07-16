import pandas as pd
import requests

# Configuration -  Space Weather Data.

SPACE_WEATHER_API_URL = "https://celestrak.org/SpaceData/SW-All.txt"

OUTPUT_FILE = "data/space_weather_data.txt"


def fetch_space_weather_data():
    """
    Fetch space weather data from CelesTrak.
    """
    try:
        print("Fetching space weather data...")
        response = requests.get(SPACE_WEATHER_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.text
        print("Space weather data fetched successfully.")
        return data
    except requests.RequestException as e:
        print(f"Error fetching space weather data: {e}")
        return None

def save_space_weather_data(data, filename=OUTPUT_FILE):
    """
    Save the fetched space weather data to a file.
    """
    try:
        with open(filename, "w") as file:
            file.write(data)
        print(f"Space weather data saved to {filename}.")

    except IOError as e: 
        print(f"Error: Could not write data to file {filename}.")
        print(e)

def main():
    """
    Main function to fetch and save the data.
    """
    space_weather_data = fetch_space_weather_data()
    if space_weather_data:
        save_space_weather_data(space_weather_data)


if __name__ == "__main__":
    main()