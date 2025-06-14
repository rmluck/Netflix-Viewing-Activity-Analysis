"""
Runs web application for the project.
"""

# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from io import BytesIO
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import viewing_activity_analysis as netflix


st.title("Netflix Viewing Activity Analysis")

uploaded_file = st.file_uploader("Upload your Netflix viewing activity CSV file", type=["csv"])
if uploaded_file:
    try:
        df = netflix.load_data(uploaded_file)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()
    
    st.header("Filters")
    st.sidebar.header("Analysis Settings")

    with open("data/time_zones.txt", "r") as time_zones_file:
        time_zones = [line.strip() for line in time_zones_file.readlines()]
    
    time_zone = st.selectbox("Select Your Time Zone", time_zones, index=time_zones.index("America/New_York"))
    df = netflix.convert_times(df, time_zone)

    profiles = ["All Profiles"] + sorted(df["Profile Name"].unique())
    profile = st.selectbox("Select a Profile", profiles)
    if profile != "All Profiles":
        df = df[df["Profile Name"] == profile]


    df = netflix.separate_types_of_content(df)

    content_types = ["All Types", "Movie", "TV Show"]
    content_type = st.selectbox("Select Content Type", content_types)
    if content_type != "All Types":
        df = df[df["Type"] == content_type]
    
    titles = ["All Titles"] + sorted(df["Name"].dropna().unique())
    title = st.selectbox("Select Title", titles)
    if title != "All Titles":
        df = df[df["Name"] == title]
    
    options = ["Viewing Frequency", "Viewing Activity Timeline", "Viewing Heat Map", "Most Watched Days", "Duration", "Most Watched Movies", "Most Watched Shows","Most Watched Episodes", "Device Types", "Countries"]

    if content_type == "Movie":
        options.remove("Most Watched Episodes")
        options.remove("Most Watched Shows")
    elif content_type == "TV Show":
        options.remove("Most Watched Movies")
        if title == "All Titles":
            options.remove("Most Watched Episodes")

    analysis_option = st.sidebar.selectbox("Choose Analysis", options)

    if "analysis_history" not in st.session_state:
        st.session_state.analysis_history = []
    
    if st.sidebar.button("Run Analysis"):
        figure = netflix.conduct_analysis(df, analysis_option, profile, content_type, title)
        st.session_state.analysis_history.append((analysis_option, figure))
    
    if st.sidebar.button("Clear All Results"):
        st.session_state.analysis_history = []

    st.subheader("Analysis Results")
    for i, (label, figure) in enumerate(reversed(st.session_state.analysis_history)):
        st.markdown(f"**{label}**")
        st.pyplot(figure)
        buffer = BytesIO()
        figure.savefig(buffer, format="png", bbox_inches="tight")
        buffer.seek(0)
        st.download_button(label="Download Figure", data=buffer, file_name=f"{label.replace(" ", "_").lower()}.png", mime="image/png", key=f"download_{i}")
        st.markdown("---")