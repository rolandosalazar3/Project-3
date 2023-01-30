import pandas as pd
schools = pd.read_csv("https://edspiezio-runyon.github.io/university_data.csv")

import plotly.express as px

fig = px.scatter_mapbox(schools, lat="latitude", lon="longitude", hover_name="Name", hover_data=["Rank_USNewsWorldReport", "city", "state_code", "yearFounded", "website"],
                        color_discrete_sequence=["blue"], zoom=4, height=1200)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()