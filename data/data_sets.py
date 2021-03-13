from gpxpy import parse
import pandas as pd
import os

data_sets = {}

def add_data_set(name, ds):
    if name not in list(data_sets.keys()):
        data_sets[f"{name}"] = ds

# def clear_env()

def get_saved_data():
    f = "Data/ExampleData.gpx"

    gpx = parse(open(f"{f}"))
    df = pd.DataFrame(columns=["waypoints", "lat", "long"])
    df["waypoints"] = [i for i in range(len(gpx.waypoints))]
    df.set_index("waypoints", inplace = True)
    df["lat"] = [gpx.waypoints[i].latitude for i in range(len(gpx.waypoints))]
    df["long"] = [gpx.waypoints[i].longitude for i in range(len(gpx.waypoints))]
    
    f = os.path.basename(os.path.normpath(f))
    add_data_set(f, df)

get_saved_data()