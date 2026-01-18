import streamlit as st
import pandas as pd
import os
from pathlib import Path

class GUI:

    def __init__(self):
        os.makedirs("data", exist_ok=True)

        try:
            self.file_path = Path("data/concerts-attended.csv")
            self.df = pd.read_csv(self.file_path, index_col=False)
        except:
            self.df = pd.DataFrame(columns=["Artist", "Tour", "Venue", "Cost"])

    def generate_concert_data_page(self):
        self.generate_add_event()
    
    def generate_add_event(self):
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            artist = st.text_input("Enter artist name")
        with col2:
            tour = st.text_input("Enter tour name")
        with col3:
            venue = st.text_input("Enter venue name")
        with col4:
            cost = st.text_input("Enter ticket cost")

        st.button("Create new event", on_click=self.add_event, args=[artist, tour, venue, cost])

        st.write(self.df)

    def add_event(self, artist, tour, venue, cost):
        new_entry = [artist, tour, venue, cost]
        if not all(new_entry):
            st.write("Please fill out all text boxes")
            return
        
        new_row = {
            "Artist": artist,
            "Tour": tour,
            "Venue": venue,
            "Cost": cost
        }

        self.df = pd.concat(
            [self.df, pd.DataFrame([new_row])],
            ignore_index=True,
        )
        self.df.to_csv(self.file_path, index=False)
        

if __name__ == "__main__":
    gui = GUI()
    gui.generate_concert_data_page()