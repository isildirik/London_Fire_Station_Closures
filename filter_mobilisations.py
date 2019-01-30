#!/usr/bin/env python3
# This script reads london fire brigade mobilisations data from original data spreadsheet.
# Filters out the unnecessary columns and subsets the dataset to 2013 and 2014 years and outputs a csv file for further use.
import pandas as pd
import time

xls_path = './original-dataset/LFB Mobilisation data from Jan 2013.xlsx'
xls_cols = 'A,B,D,E,I,P,Q,S,V'
output_csv_name = './mobilisation_data_2013_2014.csv'

start_time = time.time()

mobdf = pd.read_excel(xls_path, sheet_name='Sheet1', usecols=xls_cols)

# Subset data up to 2015 January
mobdf = mobdf[0:314249]

mobdf.to_csv(output_csv_name, index=False)

print("--- Script finished in %.4f seconds ---" % (time.time() - start_time))
