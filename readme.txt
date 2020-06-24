## Intro

In 2014, then-Mayor of London, Boris Johnson shut down 10 fire stations, despite the acknowledgement from London Fire and Emergency Planning Authority (LFEPA) that for some boroughs, the response times would increase between 1 to 45 seconds. 

This repo contains the Python scripts used for data cleansing of London Fire Brigade (LFB) incident and mobilisation records between 2009-2016, in order to visualize (on Tableau) and assess:
•	The activity levels of the stations prior to shut-down (comprared to the other stations)
•	The impact of the station closures on the response times for the effected boroughs.

## Getting raw data

London Fire Brigade (LFB) incident and mobilisation records have been downloaded from data.london.gov.uk in separate excel files: 
•	Incident records between years 2013-2016 (https://data.london.gov.uk/dataset/london-fire-brigade-incident-records)
•	Mobilisation records between years 2013-2016 (https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records)

Total file size: 150 MB

Incident records consist of all the calls made to LFB and include information on date and time of call, unique incident number, incident type and location etc.

Mobilisation records contain the information on all the fire appliances sent to each incident, including the unique mobilisation IDs, which station the appliance was sent from, times for mobilisation and arrival to the incident locations etc. 

Neither datasets had a metafile. Most columns were self-explanatory, but some required additional research. 

The active fire station addresses were obtained from http://www.london-fire.gov.uk while the shut-in station addresses were extracted using Google search – mainly real estate ads. 

## Pre-requisites

* python3 and pip3
* pandas (pip3 install pandas)
* pyproj (pip3 install pyproj)

## Preparing data for analysis

Since the dataset contains more properties and years than we are interested in, first we filter the dataset and remove the unnecessary columns and save data in CSV format for further work.

`python3 filter_incidents`
`python3 filter_mobilisations`

These generate a CSV files named `incident_data_2013_2014.csv` and `mobilisation_data_2013_2014.csv`.

## Conversion to Latitude and Longitude

In order to use tableau geocoding tools, we need to convert Eastings and Northings to Longitude and Latitude for the incident data.

`python3 add_incident_lon_lat.py`

This generates a CSV file named `incident_data_2013_2014_with_lat_lon.csv`

## Preparing Origin/Destination dataset for Tableau spider maps

We use the incidents data and for each incident we'll generate an Origin and Destination row with the latitude and longitude.
Origin will have the latitude longitude of the responding fire station.
Destination will have the latitude longitude of the incident location.

`python3 generate_spider_map_data.py`

This will create a file named `incident_spider_maps.csv`.

| OriginDesitination | PointID | PathID | Latitude | Longitude |
| ------------------ | ------- | ------ | -------- | --------- |
| ---                | ---     | ---    | ---      | ---       |

## Notes

You can use `print_csv_summary.py` script to see a summary of the selected columns.

`python3 print_csv_summary.py [csv file path]`
