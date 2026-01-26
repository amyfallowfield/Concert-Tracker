import os
import pandas as pd
from pathlib import Path

class DataManager:

    def __init__(self):
        
        os.makedirs("data", exist_ok=True)

        try:
            self.event_path = Path("data/event-data.csv")
            self.event_df = pd.read_csv(self.event_path, index_col=False)
        except:
            self.event_df = pd.DataFrame(columns=["Artist", "Tour", "Venue Name", "City", "Seat", "Cost", "Date", "Supports"])
            self.event_df.to_csv(self.event_path, index=False)

        try:
            self.location_path = Path("data/location-data.csv")
            self.location_df = pd.read_csv(self.location_path, index_col=False)
        except:
            self.location_path = pd.DataFrame(columns=["City", "Lat", "Lon"])
            self.location_path.to_csv(self.location_path, index=False)

if __name__ == "__main__":

    DataManager()