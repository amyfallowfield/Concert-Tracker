import requests
import pandas as pd
from data_manager import DataManager
from pathlib import Path

class LocationData:

    def __init__(self):
        
        self.df = DataManager().location_df

    def update_locations(self, city):
        if city not in self.df["City"]:
            lat, lon = self.get_lat_lon(city)
            new_row = {
                "City": city,
                "Lat": lat,
                "Lon": lon,
            }
            
            self.df = pd.concat(
                [self.df, pd.DataFrame([new_row])],
                ignore_index=True,
            )
            self.df.to_csv(self.file_path, index=False)

    def get_lat_lon(self, city):
        url = "https://nominatim.openstreetmap.org/search?"
        params = {
            "city": city,
            "country": "UK",
            "format": "json",
        }
        headers = {
            "User-Agent": "ConcertTracker/1.0 (https://github.com/amyfallowfield/Concert-Tracker)"
        }

        try:
            response = requests.get(url, params=params, headers=headers)
            if response.status_code != 200:
                raise RuntimeError("Status code:", response.status_code)
            data = response.json()
        except Exception as e:
            print("Error calling Geocode API:", e)

        return data[0]["lat"], data[0]["lon"]

if __name__ == "__main__":
    data = LocationData()