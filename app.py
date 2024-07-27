import numpy as np
import pandas as pd
import matplotlib as plt
import plotly.graph_objects as go
import plotly.express as px
import dash
import streamlit as st

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

latlong = pd.read_csv('district wise centroids.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title("India's Visualization")

selected_state = st.sidebar.selectbox('Select a State', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
Secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represent primary parameter')
    st.text('Color represent Secondary Parameter')

    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', zoom=3, mapbox_style='carto-positron' , size = primary,
                                color=Secondary, size_max=30, width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=3, mapbox_style='carto-positron',
                                size=primary, color=Secondary, size_max=30, width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)