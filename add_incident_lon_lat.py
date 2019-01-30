#!/usr/bin/env python3
# This script adds Longitude and Latitude information to the incidents data by converting Esting and Northing using pyproj.
import pandas
import time
import pyproj

input_csv_path = 'incident_data_2013_2014.csv'
output_csv_path = 'incident_data_2013_2014_with_lat_lon.csv'

start_time = time.time()

df = pandas.read_csv(input_csv_path)

# Ordnance Survey British National Grid System (easting, northing)
bng = pyproj.Proj(init='epsg:27700')
# World GPS Sattelite Grid System (lat, lon)
wgs84 = pyproj.Proj(init='epsg:4326')

# Converts from BNG to WGS
# def convert_coordinates(row):
#     lon, lat = pyproj.transform(bng, wgs84, row['Easting'], row['Northing'])
#     return pandas.Series({'Longitude': lon, 'Latitude': lat})
# Apply the conversion to each row and append the results into the dataframe as columns
# df = df.join(df.apply(convert_coordinates, axis=1))

# We use a for loop instead of the above commented apply version, as this uses less memory and runs faster.
lons, lats = [], []
for _, row in df.iterrows():
    lon, lat = pyproj.transform(bng, wgs84, row['Easting'], row['Northing'])
    lons.append(lon)
    lats.append(lat)
lon_lat_df = pandas.DataFrame({'Longitude': lons, 'Latitude': lats})
df = df.join(lon_lat_df)

df.info()

df.to_csv(output_csv_path, index=False)

print("--- Script finished in %.4f seconds ---" % (time.time() - start_time))
