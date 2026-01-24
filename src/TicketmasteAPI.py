import requests
import pandas as pd
import json
from pathlib import Path

class LocationData:

    API_KEY = "l5CurktVqxvRnRKreAG1M1EAnkCw6SPo"
    URL_BASE = "https://app.ticketmaster.com/discovery/v2/"

    def __init__(self):

        try:
            self.file_path = Path("data/venue-location-data.csv")
            self.df = pd.read_csv(self.file_path, index_col=False)
        except:
            self.df = pd.DataFrame(columns=["Venue", "Location", "Latitude", "Longitude"])

        self.get_venue_data()

    def get_venue_data(self):
        url = self.URL_BASE + "/venues"

        params = {
            "apikey": self.API_KEY,
            "countryCode": "UK",
        }

        with open("Ticketmaster.json", "w", encoding="utf-8") as f:
            page = 0
            end = 1
            final_data = []

            while(page < end):
                params["page"] = page
                try:
                    response = requests.get(url, params=params)
                    data = response.json()
                    #venue_data = data["_embedded"]["venues"]
                    venue_data = self.simplify_venue_data(data["_embedded"]["venues"])
                    if response.status_code != 200:
                        raise RuntimeError("API call to retrieve venue ID failed")
                except Exception as e:
                    print("Error fetching venue id:", e)
                    break
                
                end = data["page"]["totalPages"]
                final_data += venue_data
                page += 1

            json.dump(final_data, f, ensure_ascii=False, indent=4)

    def simplify_venue_data(self, data):
        final_data = []
        for i in range(len(data)):

            if "city" in data[i]:
                city = data[i]["city"]["name"]
            else:
                city = {}
            
            final_data.append({
                "name": data[i]["name"],
                "id": data[i]["id"],
                "city": city,
            })
        return final_data

if __name__ == "__main__":
    data = LocationData()