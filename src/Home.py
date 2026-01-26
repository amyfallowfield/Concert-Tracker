import streamlit as st
from data_manager import DataManager

class GUI:

    def __init__(self):

        st.set_page_config(page_title="Concert Tracker", layout="wide")
        st.navigation(["Events.py", "Statistics.py"])

        pages = {
            "Event History": [
                st.Page("Events.py", title="Events"),
                st.Page("Statistics.py", title="Statistics"),
            ],
        }

        pg = st.navigation(pages)
        pg.run()

if __name__ == "__main__":

    GUI()