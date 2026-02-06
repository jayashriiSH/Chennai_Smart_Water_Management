import geopandas as gpd

# Load UGT KML
ugt = gpd.read_file("underhead.kml", driver="KML")

# Convert CRS
ugt = ugt.to_crs(epsg=4326)

# Create centroids if polygon
ugt["geometry"] = ugt.geometry.centroid

# Save
ugt.to_file("ugt_points.geojson", driver="GeoJSON")

print("✅ UGT points created")
