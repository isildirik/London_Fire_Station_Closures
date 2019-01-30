#!/usr/bin/env python3
# This script generate origin/destination data source for incident spider maps
import pandas
import time

stations_xls_path = './original-dataset/FireStationLatLon.xlsx'
incidents_csv_path = './incident_data_2013_2014_with_lat_lon.csv'
map_data_csv_path = './spider_map_data.csv'

stations_xls_cols = 'A,B,E,F'
incidents_csv_cols = [
    'IncidentNumber', 'CalYear', 'BoroughName', 'WardName',
    'IncidentStationGround', 'Latitude', 'Longitude'
]

start_time = time.time()

stations_df = pandas.read_excel(
    stations_xls_path,
    sheet_name='to_Tableau',
    usecols=stations_xls_cols,
    index_col=0)

incidents_df = pandas.read_csv(incidents_csv_path, usecols=incidents_csv_cols)
# incidents_df = incidents_df.head(11100)

number_of_incidents = len(incidents_df)

ods, pointids, pathids, lons, lats, boroughs, calyears = [], [], [], [], [], [], []
for i, incident in incidents_df.iterrows():
    station_name = incident['IncidentStationGround']
    if station_name == 'OverTheBorder':
        continue
    if i % 1000 == 0:
        print("%2.1f%% complete\r" % (i / number_of_incidents * 100), end='')

    station = stations_df.loc[station_name]

    incident_number = str(incident['IncidentNumber'])
    station_lon = station['Longitude']
    station_lat = station['Latitude']
    incident_lon = incident['Longitude']
    incident_lat = incident['Latitude']
    borough = incident['BoroughName']
    calyear = incident['CalYear']
    path_id = station_name + '_' + str(incident['IncidentNumber'])

    ods.append('Origin')
    ods.append('Destination')

    pointids.append(station_name)
    pointids.append(incident_number)

    pathids.append(path_id)
    pathids.append(path_id)

    lons.append(station_lon)
    lons.append(incident_lon)

    lats.append(station_lat)
    lats.append(incident_lat)

    boroughs.append(borough)
    boroughs.append(borough)

    calyears.append(calyear)
    calyears.append(calyear)

map_df = pandas.DataFrame({
    'OriginDestination': ods,
    'PointID': pointids,
    'PathID': pathids,
    'Longitude': lons,
    'Latitude': lats,
    'BoroughName': boroughs,
    'CalYear': calyears
})

print("")
map_df.to_csv(map_data_csv_path, index=False)

print("--- Script finished in %.4f seconds ---" % (time.time() - start_time))
