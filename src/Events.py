import streamlit as st
import pandas as pd
from data_manager import DataManager

class EventsPage:

    def __init__(self):

        self.df = DataManager().event_df
        st.title("Events")

        self.generate_add_event()
        self.generate_view_events()

    def generate_add_event(self):
        
        col1, col2, col3 = st.columns(3)
        with col1:
            artist = st.text_input("Enter artist name")
            venue_city = st.text_input("Enter city")
            date = st.date_input("Enter date", value="today", format="DD/MM/YYYY")
        with col2:
            tour = st.text_input("Enter tour name")
            seat = st.text_input("Enter seat or GA")
            cost = st.number_input("Enter ticket cost")
        with col3:
            venue_name = st.text_input("Enter venue name")
            supports = st.text_area("Enter support(s) [Separate each artist with a comma]")
            
        supports_list = supports.split(",")
        for i in supports_list:
            i.strip()

        st.button("Create new event", on_click=self.add_event, args=[artist, venue_city, date, tour, seat, cost, venue_name, supports_list])

    def generate_view_events(self):
        st.dataframe(self.df)

    def add_event(self, artist, venue_city, date, tour, seat, cost, venue_name, supports_list):

        new_entry = [artist, venue_city, date, tour, seat, venue_name, supports_list, cost]
        if not all(new_entry[:-3]):
            st.write("Please fill out all text boxes")
            return

        new_row = {
            "Artist": artist,
            "Tour": tour,
            "Venue Name": venue_name,
            "City": venue_city,
            "Seat": seat,
            "Cost": cost,
            "Date": date,
            "Supports": supports_list,
        }

        self.dm.concert_df = pd.concat(
            [self.dm.concert_df, pd.DataFrame([new_row])],
            ignore_index=True,
        )
        self.dm.concert_df.to_csv(self.dm.event_path, index=False)

        self.location.update_locations(venue_city)

if __name__ == "__main__":
    page = EventsPage()