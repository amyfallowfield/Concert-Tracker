import streamlit as st
from data_manager import DataManager

class GUI:

    def __init__(self):

        st.set_page_config(page_title="Concert Tracker", layout="wide")
        st.navigation(["Home.py", "Events.py", "Statistics.py"])

        st.write("I will input tutorial stuff here :)")

if __name__ == "__main__":

    GUI()