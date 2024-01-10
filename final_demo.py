from PIL import Image
import streamlit as st
import pandas as pd

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

if  Selected_IMO == 9454462 and Routes == 'route01':
    st.subheader("Vessel Information")
    col1, col2, col3, col4 = st.columns(4)
    col1.info(f"**Vessel Name:** {group_9454462_r1['name'].iloc[0]}")
    col2.info(f"**Vessel Type:** {group_9454462_r1['type_specific'].iloc[0]}")
    col3.info(f"**Avg Vessel Speed:** {round(group_9454462_r1['speed'].mean(), 2)} m/s")
    
    col4.info(f"**Avg Wind Pressure:** {round(group_9454462_r1['main.pressure'].mean(), 2)} hPa")
    col5, col6, col7, col8 = st.columns(4)
    col5.info(f"**Avg Wind Speed:** {round(group_9454462_r1['wind.speed'].mean(), 2)} m/s")
    col6.info(f"**Vessel IMOs:** {group_9454462_r1['imo'].iloc[0]}")
    
    col7.info(f"**Vessel MMSIs:** {group_9454462_r1['mmsi'].iloc[0]}")
    col8.info(f"**Country Code:** {group_9454462_r1['country_iso'].iloc[0]}")
    
    col9, col10 = st.columns(2)
    col9.info(f"**Departure:** {group_9454462_r1['departure'].iloc[0]}")
    col10.info(f"**Arrival:** {group_9454462_r1['destination'].iloc[0]}")

    file_path = '(9454462)route01.html'
    with open(file_path, 'r') as f:
        html_data = f.read()

    st.subheader("Vessel Locator Map")
    st.components.v1.html(html_data, height=700)

    st.subheader("Plots")
    
    col1, col2 = st.columns(2)

# Load and display images in columns
    with col1:
        image_1 = Image.open('(9454462)kpi(R1).png')
        st.image(image_1, caption='Environmental Conditions Along Vessel Route')

        image_4 = Image.open('(9454462)speed(R1).png')
        st.image(image_4, caption='Speed En Route')


    with col2:
        image_3 = Image.open('(9454462)speed_frequency(R1).png')
        st.image(image_3, caption='Charting Speed: Navigating Frequencies En Route')

        image_2 = Image.open('(9454462)weather_frequency(R1).png')
        st.image(image_2, caption="Nature's Rhythms: Weather Frequencies in Motion")


elif  Selected_IMO == 9454462 and Routes == 'route02':
    st.subheader("Vessel Information")
    col1, col2, col3, col4 = st.columns(4)
    col1.info(f"**Vessel Name:** {group_9454462_r2['name'].iloc[0]}")
    col2.info(f"**Vessel Type:** {group_9454462_r2['type_specific'].iloc[0]}")
    col3.info(f"**Avg Vessel Speed:** {round(group_9454462_r2['speed'].mean(), 2)} m/s")
    
    col4.info(f"**Avg Wind Pressure:** {round(group_9454462_r2['main.pressure'].mean(), 2)} hPa")
    col5, col6, col7, col8 = st.columns(4)
    col5.info(f"**Avg Wind Speed:** {round(group_9454462_r2['wind.speed'].mean(), 2)} m/s")
    col6.info(f"**Vessel IMOs:** {group_9454462_r2['imo'].iloc[0]}")
    
    col7.info(f"**Vessel MMSIs:** {group_9454462_r2['mmsi'].iloc[0]}")
    col8.info(f"**Country Code:** {group_9454462_r2['country_iso'].iloc[0]}")

    col9, col10 = st.columns(2)
    col9.info(f"**Departure:** {group_9454462_r2['departure'].iloc[0]}")
    col10.info(f"**Arrival:** {group_9454462_r2['destination'].iloc[0]}")

    file_path = '(9454462)route02.html'
    with open(file_path, 'r') as f:
        html_data = f.read()

    st.subheader("Vessel Locator Map")
    st.components.v1.html(html_data, height=700)

    st.subheader("Plots")
    
    col1, col2 = st.columns(2)

# Load and display images in columns
    with col1:
        image_1 = Image.open('(9454462)kpi(R2).png')
        st.image(image_1, caption='Environmental Conditions Along Vessel Route')

        image_4 = Image.open('(9454462)speed(R2).png')
        st.image(image_4, caption='Speed En Route')

    with col2:
        image_3 = Image.open('(9454462)speed_frequency(R2).png')
        st.image(image_3, caption='Charting Speed: Navigating Frequencies En Route')

        image_2 = Image.open('(9454462)weather_frequency(R2).png')
        st.image(image_2, caption="Nature's Rhythms: Weather Frequencies in Motion")

elif  Selected_IMO == 9454462 and Routes == 'route03':
    st.subheader("Vessel Information")
    col1, col2, col3, col4 = st.columns(4)
    col1.info(f"**Vessel Name:** {group_9454462_r3['name'].iloc[0]}")
    col2.info(f"**Vessel Type:** {group_9454462_r3['type_specific'].iloc[0]}")
    col3.info(f"**Avg Vessel Speed:** {round(group_9454462_r3['speed'].mean(), 2)} m/s")
    
    col4.info(f"**Avg Wind Pressure:** {round(group_9454462_r3['main.pressure'].mean(), 2)} hPa")
    col5, col6, col7, col8 = st.columns(4)
    col5.info(f"**Avg Wind Speed:** {round(group_9454462_r3['wind.speed'].mean(), 2)} m/s")
    col6.info(f"**Vessel IMOs:** {group_9454462_r3['imo'].iloc[0]}")
    
    col7.info(f"**Vessel MMSIs:** {group_9454462_r3['mmsi'].iloc[0]}")
    col8.info(f"**Country Code:** {group_9454462_r3['country_iso'].iloc[0]}")
    
    col9, col10 = st.columns(2)
    col9.info(f"**Departure:** {group_9454462_r3['departure'].iloc[0]}")
    col10.info(f"**Arrival:** {group_9454462_r3['destination'].iloc[0]}")

    file_path = '(9454462)route03.html'
    with open(file_path, 'r') as f:
        html_data = f.read()

    st.subheader("Vessel Locator Map")
    st.components.v1.html(html_data, height=700)

    st.subheader("Plots")
    
    col1, col2 = st.columns(2)

# Load and display images in columns
    with col1:
        image_1 = Image.open('(9454462)kpi(R3).png')
        st.image(image_1, caption='Environmental Conditions Along Vessel Route')

        image_4 = Image.open('(9454462)speed(R3).png')
        st.image(image_4, caption='Speed En Route')

    with col2:
        image_3 = Image.open('(9454462)speed_frequency(R3).png')
        st.image(image_3, caption='Charting Speed: Navigating Frequencies En Route')

        image_2 = Image.open('(9454462)weather_frequency(R3).png')
        st.image(image_2, caption="Nature's Rhythms: Weather Frequencies in Motion")

elif Selected_IMO == 9301201 and Routes == 'route01':
    st.subheader("Vessel Information")
    col1, col2, col3, col4 = st.columns(4)
    col1.info(f"**Vessel Name:** {group_9301201_r1['name'].iloc[0]}")
    col2.info(f"**Vessel Type:** {group_9301201_r1['type_specific'].iloc[0]}")
    col3.info(f"**Avg Vessel Speed:** {round(group_9301201_r1['speed'].mean(), 2)} m/s")
    
    col4.info(f"**Avg Wind Pressure:** {round(group_9301201_r1['main.pressure'].mean(), 2)} hPa")
    col5, col6, col7, col8 = st.columns(4)
    col5.info(f"**Avg Wind Speed:** {round(group_9301201_r1['wind.speed'].mean(), 2)} m/s")
    col6.info(f"**Vessel IMOs:** {group_9301201_r1['imo'].iloc[0]}")
    
    col7.info(f"**Vessel MMSIs:** {group_9301201_r1['mmsi'].iloc[0]}")
    col8.info(f"**Country Code:** {group_9301201_r1['country_iso'].iloc[0]}")
    
    col9, col10 = st.columns(2)
    col9.info(f"**Departure:** {group_9301201_r1['departure'].iloc[0]}")
    col10.info(f"**Arrival:** {group_9301201_r1['destination'].iloc[0]}")

    file_path = '(9301201)route01.html'
    with open(file_path, 'r') as f:
        html_data = f.read()

    st.subheader("Vessel Locator Map")
    st.components.v1.html(html_data, height=700)

    st.subheader("Plots")
    
    col1, col2 = st.columns(2)

# Load and display images in columns
    with col1:
        image_1 = Image.open('(9301201)kpi(R1).png')
        st.image(image_1, caption='Environmental Conditions Along Vessel Route')

        image_4 = Image.open('(9301201)speed(R1).png')
        st.image(image_4, caption='Speed En Route')

    with col2:
        image_3 = Image.open('(9301201)speed_frequency(R1).png')
        st.image(image_3, caption='Charting Speed: Navigating Frequencies En Route')

        image_2 = Image.open('(9301201)weather_frequency(R1).png')
        st.image(image_2, caption="Nature's Rhythms: Weather Frequencies in Motion")

elif Selected_IMO == 9301201 and Routes == 'route02':
    st.subheader("Vessel Information")
    col1, col2, col3, col4 = st.columns(4)
    col1.info(f"**Vessel Name:** {group_9301201_r2['name'].iloc[0]}")
    col2.info(f"**Vessel Type:** {group_9301201_r2['type_specific'].iloc[0]}")
    col3.info(f"**Avg Vessel Speed:** {round(group_9301201_r2['speed'].mean(), 2)} m/s")
    
    col4.info(f"**Avg Wind Pressure:** {round(group_9301201_r2['main.pressure'].mean(), 2)} hPa")
    col5, col6, col7, col8 = st.columns(4)
    col5.info(f"**Avg Wind Speed:** {round(group_9301201_r2['wind.speed'].mean(), 2)} m/s")
    col6.info(f"**Vessel IMOs:** {group_9301201_r2['imo'].iloc[0]}")
    
    col7.info(f"**Vessel MMSIs:** {group_9301201_r2['mmsi'].iloc[0]}")
    col8.info(f"**Country Code:** {group_9301201_r2['country_iso'].iloc[0]}")
    
    col9, col10 = st.columns(2)
    col9.info(f"**Departure:** {group_9301201_r2['departure'].iloc[0]}")
    col10.info(f"**Arrival:** {group_9301201_r2['destination'].iloc[0]}")

    file_path = '(9301201)route02.html'
    with open(file_path, 'r') as f:
        html_data = f.read()

    st.subheader("Vessel Locator Map")
    st.components.v1.html(html_data, height=700)

    st.subheader("Plots")
    
    col1, col2 = st.columns(2)

# Load and display images in columns
    with col1:
        image_1 = Image.open('(9301201)kpi(R2).png')
        st.image(image_1, caption='Environmental Conditions Along Vessel Route')

        image_4 = Image.open('(9301201)speed(R2).png')
        st.image(image_4, caption='Speed En Route')

    with col2:
        image_3 = Image.open('(9301201)speed_frequency(R2).png')
        st.image(image_3, caption='Charting Speed: Navigating Frequencies En Route')

        image_2 = Image.open('(9301201)weather_frequency(R2).png')
        st.image(image_2, caption="Nature's Rhythms: Weather Frequencies in Motion")

elif Selected_IMO == 9301201 and Routes == 'route03':
    st.subheader("Vessel Information")
    col1, col2, col3, col4 = st.columns(4)
    col1.info(f"**Vessel Name:** {group_9301201_r3['name'].iloc[0]}")
    col2.info(f"**Vessel Type:** {group_9301201_r3['type_specific'].iloc[0]}")
    col3.info(f"**Avg Vessel Speed:** {round(group_9301201_r3['speed'].mean(), 2)} m/s")
    
    col4.info(f"**Avg Wind Pressure:** {round(group_9301201_r3['main.pressure'].mean(), 2)} hPa")
    col5, col6, col7, col8 = st.columns(4)
    col5.info(f"**Avg Wind Speed:** {round(group_9301201_r3['wind.speed'].mean(), 2)} m/s")
    col6.info(f"**Vessel IMOs:** {group_9301201_r3['imo'].iloc[0]}")
    
    col7.info(f"**Vessel MMSIs:** {group_9301201_r3['mmsi'].iloc[0]}")
    col8.info(f"**Country Code:** {group_9301201_r3['country_iso'].iloc[0]}")

    col9, col10 = st.columns(2)
    col9.info(f"**Departure:** {group_9301201_r3['departure'].iloc[0]}")
    col10.info(f"**Arrival:** {group_9301201_r3['destination'].iloc[0]}")

    file_path = '(9301201)route03.html'
    with open(file_path, 'r') as f:
        html_data = f.read()

    st.subheader("Vessel Locator Map")
    st.components.v1.html(html_data, height=700)

    st.subheader("Plots")
    
    col1, col2 = st.columns(2)

# Load and display images in columns
    with col1:
        image_1 = Image.open('(9301201)kpi(R3).png')
        st.image(image_1, caption='Environmental Conditions Along Vessel Route')

        image_4 = Image.open('(9301201)speed(R3).png')
        st.image(image_4, caption='Speed En Route')


    with col2:
        image_3 = Image.open('(9301201)speed_frequency(R3).png')
        st.image(image_3, caption='Charting Speed: Navigating Frequencies En Route')

        image_2 = Image.open('(9301201)weather_frequency(R3).png')
        st.image(image_2, caption="Nature's Rhythms: Weather Frequencies in Motion")

else:
    st.write("Data Not Available")
