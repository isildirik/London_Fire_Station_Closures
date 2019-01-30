#!/usr/bin/env python3
# This script reads london fire brigade incident data from original data spreadsheet.
# Filters out the unnecessary columns and subsets the dataset to 2013 and 2014 years and outputs a csv file for further use.
import pandas as pd
import time

xls_path = './original-dataset/LFB Incident data from January 2013 to December 2016.xlsx'
output_csv_name = './incident_data_2013_2014.csv'

start_time = time.time()

df = pd.read_excel(xls_path, sheet_name='Incidents', usecols='A,B,C,D,F,G,I,M,N,O,Q,R,V,W,Y')

# Rename some colums
df.rename(
    index=str,
    columns={
        "IncGeo_BoroughCode": "BoroughCode",
        "IncGeo_WardCode": "WardCode",
        "IncGeo_BoroughName": "BoroughName",
        "IncGeo_WardName": "WardName",
        "Easting_rounded": "Easting",
        "Northing_rounded": "Northing"
    },
    inplace=True)

# Subset data before 2015
df = df[df["CalYear"] < 2015]

df.to_csv(output_csv_name, index=False)

print("--- Script finished in %.4f seconds ---" % (time.time() - start_time))
