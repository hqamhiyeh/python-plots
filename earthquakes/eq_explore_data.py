from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path(__file__).resolve().parent / 'data' \
    / 'eq_data_30_day_m1.geojson'
contents = path.read_text()
all_eq_data = json.loads(contents)

# Extract title of dataset
title = all_eq_data['metadata']['title']

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append( eq_dict['properties']['mag'] )
    lons.append( eq_dict['geometry']['coordinates'][0] )
    lats.append( eq_dict['geometry']['coordinates'][1] )
    eq_titles.append( eq_dict['properties']['title'] )

fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color':'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()
