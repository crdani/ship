from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns

Route = pd.read_csv("Marine_routes.csv")

trip_option = Route["routes"].unique()
imo_options = Route["imo"].unique().tolist()
grouped_data = Route.groupby(['imo', 'routes'])

group_9454462_r1 = grouped_data.get_group((9454462, 'route01'))
group_9454462_r2 = grouped_data.get_group((9454462, 'route02'))
group_9454462_r3 = grouped_data.get_group((9454462, 'route03'))
group_9301201_r1 = grouped_data.get_group((9301201, 'route01'))
group_9301201_r2 = grouped_data.get_group((9301201, 'route02'))
group_9301201_r3 = grouped_data.get_group((9301201, 'route03'))

st.set_page_config(page_title="Vessels", 
                   page_icon=":ship:", 
                   layout="wide",
                   initial_sidebar_state="expanded")

st.sidebar.image("ship.jpg", width=100, use_column_width=True)
st.sidebar.header("Vessel Dashboard")

Selected_IMO = st.sidebar.selectbox("Select IMO", imo_options, 0)
Routes = st.sidebar.selectbox("Select Route", trip_option, 0)

st.title("Marine Route Info")
# st.header("Fuse ship paths with dynamic weather, creating a captivating visual blend!")
# data = [group_9454462_r1["speed"]]
# group_labels= ["speed"]
def plot_speed_histogram(data):
    speed_fig = px.histogram(data, x="speed")
    speed_fig.update_layout(
        bargap=0.2,
        width=900,
        height=400,
        title='Speed Distribution',
        title_x=0.3,
        title_font=dict(size=24)
    )
    speed_fig.update_traces(marker=dict(color='skyblue'))
    st.plotly_chart(speed_fig, theme="streamlit")
speed_fig = px.histogram(group_9454462_r1, x="speed")
speed_fig.update_layout(bargap=0.2, width=900, height=400, title='Speed Distribution', title_x=0.3, title_font=dict(size=24)) # Set width and height
speed_fig.update_traces(marker=dict(color='skyblue'))  # Change 'green' to your desired color
# Displaying the plot using Streamlit
#st.plotly_chart(speed_fig, theme="streamlit", use_container_width=True)

# speed_time = plt.figure(figsize=(10, 4))
# sns.lineplot(data=group_9454462_r1[['speed', 'wind.speed']])
# plt.xlabel('Time')
# plt.ylabel('Speed (m/s)')
# plt.legend(['Vessel Speed', 'Wind Speed'])
speed_time = plt.figure(figsize=(9, 4))

# Assuming group_9454462_r1 is your DataFrame
sns.lineplot(data=group_9454462_r1[['speed', 'wind.speed']])
plt.xlabel('Time', color='white')
plt.ylabel('Speed (m/s)', color='white')

# Change legend text color
plt.legend(['Vessel Speed', 'Wind Speed'])
leg = plt.gca().get_legend()
text_color = 'white'
for text in leg.get_texts():
    plt.setp(text, color = text_color)

# Change ticks color
plt.tick_params(axis='x', colors='white')
plt.tick_params(axis='y', colors='white')
plt.title('                                                             Vessel Speed vs Wind Speed', color='white', fontsize=24, loc='center')


kpi_chart = plt.figure(figsize=(9, 4))

# Assuming group_9454462_r1 is your DataFrame
sns.lineplot(data=group_9454462_r1[['main.temp', 'main.humidity', "main.pressure"]])
plt.xlabel('Time', color='white')
plt.ylabel('Value', color='white')

# Change legend text color
plt.legend(['Temperature(K)', 'Humidity', 'Pressure(hPA)'])
leg = plt.gca().get_legend()
text_color = 'white'
for text in leg.get_texts():
    plt.setp(text, color = text_color)

# Change ticks color
plt.tick_params(axis='x', colors='white')
plt.tick_params(axis='y', colors='white')
#plt.suptitle('Environmental Conditions Along Vessel Routes', color='white', fontsize=24)
title= plt.title('                                            Environmental Conditions Along Vessel Routes', color='white', fontsize=24)

st.subheader("Plots")

cloud_cover = px.histogram(group_9454462_r1, x="description")
cloud_cover.update_layout(bargap=0.2, width=900, height=400, title='Cloud Condition', title_x=0.3, title_font=dict(size=24))  # Set width and height
cloud_cover.update_traces(marker=dict(color='skyblue'))  # Change 'green' to your desired color
cloud_cover.update_xaxes(tickangle=-45)
# Displaying the plot using Streamlit
#st.plotly_chart(cloud_cover, theme="streamlit", use_container_width=True)

col1, col2 = st.columns(2)

    # Load and display images in columns
with col1:
    st.plotly_chart(speed_fig, theme="streamlit")
    st.plotly_chart(cloud_cover, theme="streamlit")
    
with col2:
    st.plotly_chart(kpi_chart, theme="streamlit")
    st.plotly_chart(speed_time, theme="streamlit")
