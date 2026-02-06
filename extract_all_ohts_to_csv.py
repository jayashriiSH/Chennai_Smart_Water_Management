import json
import pandas as pd

# -------- INPUT FILE --------
INPUT_GEOJSON = "overhead_tanks_points.geojson"
OUTPUT_CSV = "oht_master_dataset.csv"

# -------- LOAD DATA --------
with open(INPUT_GEOJSON, "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

for feature in data["features"]:
    props = feature["properties"]
    geom = feature["geometry"]

    row = {
        "oht_id": props.get("oht_id"),
        "name": props.get("name_of_the_wds"),
        "depot": props.get("depot"),
        "capacity_ml": props.get("capacity_of_oht_ml"),
        "depth_m": props.get("depth_of_oht_m"),
        "inlets": props.get("no_of_inlets"),
        "outlets": props.get("no_of_outlets"),
        "water_source_ugt": props.get("water_received_from_id"),
        "longitude": geom["coordinates"][0],
        "latitude": geom["coordinates"][1]
    }

    rows.append(row)

# -------- CREATE CSV --------
df = pd.DataFrame(rows)

df.to_csv(OUTPUT_CSV, index=False)

print("✅ ALL OHTs extracted successfully")
print(df.head())
print("Total OHTs:", len(df))
