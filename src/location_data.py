import requests
import pandas as pd
import json
import time
from pathlib import Path

class LocationData:

    # Ticketmaster
    API_KEY = "l5CurktVqxvRnRKreAG1M1EAnkCw6SPo"
    URL_BASE = "https://app.ticketmaster.com/discovery/v2/"

    def __init__(self):
        pass

if __name__ == "__main__":
    data = LocationData()