import geopandas as gpd

# Load polygon GeoJSON
gdf = gpd.read_file("overhead_tanks.geojson")

# Create centroid
gdf["geometry"] = gdf.geometry.centroid

# Save as point GeoJSON
gdf.to_file("overhead_tanks_points.geojson", driver="GeoJSON")
