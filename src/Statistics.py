import streamlit as st
import plotly.express as px
from data_manager import DataManager

class StatsPage:

    def __init__(self):

        st.title("Statistics")
        self.dm = DataManager()
        self.df = self.dm.event_df

        if len(self.df) > 0:
            self.generate_summary()
            self.generate_map()
        else:
            st.write("Add your first event in the \"Events\" tab first")

    def generate_summary(self):
        cost = round(self.df["Cost"].sum(), 2)
        shows = len(self.df)
        fav_artist_name = self.df["Artist"].mode()[0]
        fav_artist_count = self.df[self.df["Artist"] == fav_artist_name]["Artist"].count()
        fav_venue_name = self.df["Venue Name"].mode()[0]
        fav_venue_count = self.df[self.df["Venue Name"] == fav_venue_name]["Venue Name"].count()

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Spent", f"£{cost}")
        with col2:
            st.metric("Total Shows", shows)
        with col3:
            st.metric("Favourite Artist", f"{fav_artist_name} (x{fav_artist_count})")
        with col4:
            st.metric("Favourite Venue", f"{fav_venue_name} (x{fav_venue_count})")

    def generate_map(self):

        UK_BOUNDS = {
            "west": -10.5,
            "east": 2.2,
            "south": 51.3,
            "north": 56.5,
        }

        fig = px.density_mapbox(
            self.generate_map_data(),
            lat="Lat",
            lon="Lon",
            z="Count",
            radius=40,
            zoom=0,
        )

        fig.update_layout(
            margin={"r":0,"t":0,"l":0,"b":0},
            width=1000,
            height=800,
            mapbox = dict(
                style="open-street-map",
                center={"lat": 55, "lon": -3.0},
                bounds=UK_BOUNDS,
            ),
        )

        st.plotly_chart(fig, width="content")

    def generate_map_data(self):
        city_counts = (
            self.df.groupby("City")
            .size().
            reset_index(name="Count")
        )

        map_df = city_counts.merge(
            self.dm.location_df,
            on="City",
            how="left",
        )

        map_df.to_csv("data/map-data.csv", index=False)
        return map_df

if __name__ == "__main__":
    StatsPage()