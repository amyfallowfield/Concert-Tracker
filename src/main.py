import streamlit as st
import pandas as pd
import os
from pathlib import Path
import TicketmasteAPI

class GUI:

    def __init__(self):
        os.makedirs("data", exist_ok=True)
        self.api = TicketmasteAPI.LocationData()

        try:
            self.file_path = Path("data/concerts-attended.csv")
            self.df = pd.read_csv(self.file_path, index_col=False)
        except:
            self.df = pd.DataFrame(columns=["Artist", "Tour", "Venue", "Cost"])

        st.set_page_config(page_title="Concert Tracker", layout="wide")

        self.generate_concert_data_page()

    def generate_concert_data_page(self):
        if len(self.df) > 0:
            self.generate_summary()
        else:
            st.write("Add your first event here")

        self.generate_add_event()
        self.generate_view_events()
    
    def generate_summary(self):
        cost = round(self.df["Cost"].sum(), 2)
        shows = len(self.df)
        fav_artist_name = self.df["Artist"].mode()[0]
        fav_artist_count = self.df[self.df["Artist"] == fav_artist_name]["Artist"].count()
        fav_venue_name = self.df["Venue"].mode()[0]
        fav_venue_count = self.df[self.df["Venue"] == fav_venue_name]["Venue"].count()

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Spent", f"£{cost}")
        with col2:
            st.metric("Total Shows", shows)
        with col3:
            st.metric("Favourite Artist", f"{fav_artist_name} (x{fav_artist_count})")
        with col4:
            st.metric("Favourite Venue", f"{fav_venue_name} (x{fav_venue_count})")

    def generate_view_events(self):
        st.dataframe(self.df)

    def generate_add_event(self):
        
        col1, col2, col3 = st.columns(3)
        with col1:
            artist = st.text_input("Enter artist name")
            date = st.date_input("Enter date", value="today", format="DD/MM/YYYY")
        with col2:
            tour = st.text_input("Enter tour name")
            cost = st.number_input("Enter ticket cost")
        with col3:
            venue = st.text_input("Enter venue name")
            supports = st.text_area("Enter support(s) [Separate each artist with a comma]")
            
        supports_list = supports.split(",")
        for i in supports_list:
            i.strip()

        st.button("Create new event", on_click=self.add_event, args=[artist, tour, venue, cost, date, supports_list])

    def add_event(self, artist, tour, venue, cost, date, supports):

        new_entry = [artist, tour, venue, date, cost, supports]
        if not all(new_entry[:-3]):
            st.write("Please fill out all text boxes")
            return

        new_row = {
            "Artist": artist,
            "Tour": tour,
            "Venue": venue,
            "Location": self.api.get_location_data(venue),
            "Cost": cost,
            "Date": date,
            "Supports": supports,
        }

        self.df = pd.concat(
            [self.df, pd.DataFrame([new_row])],
            ignore_index=True,
        )
        self.df.to_csv(self.file_path, index=False)

if __name__ == "__main__":
    gui = GUI()