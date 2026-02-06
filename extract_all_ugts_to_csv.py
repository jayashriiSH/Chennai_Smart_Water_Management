import json
import pandas as pd

# -------- INPUT --------
INPUT_GEOJSON = "ugt_points.geojson"
OUTPUT_CSV = "ugt_master_dataset.csv"

# -------- LOAD GEOJSON --------
with open(INPUT_GEOJSON, "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

for feature in data["features"]:
    props = feature["properties"]
    geom = feature["geometry"]

    row = {
        "ugt_id": props.get("ugt_id"),
        "name": props.get("name_of_the_wds"),
        "wds_id": props.get("wds_id"),
        "capacity_ml": props.get("capacity_of_ugt_ml"),
        "depth_m": props.get("depth_of_ugt_m"),
        "inlets": props.get("no_of_inlets"),
        "components": props.get("no_of_components"),
        "water_source": props.get("water_received_from_id"),
        "longitude": geom["coordinates"][0],
        "latitude": geom["coordinates"][1]
    }

    rows.append(row)

# -------- CREATE CSV --------
df = pd.DataFrame(rows)

df.to_csv(OUTPUT_CSV, index=False)

print("✅ UGT master CSV created successfully")
print(df.head())
print("Total UGTs:", len(df))
