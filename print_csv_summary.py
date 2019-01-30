#!/usr/bin/env python3
import sys
import pandas
import time

start_time = time.time()

csv_file_path = sys.argv[1]

df = pandas.read_csv(csv_file_path, index_col=0)

print(df.index)
print('---')
print(df.columns)
print('---')
print(df.shape)
print('---')
df.info()
print('---')

print("--- Script finished in %.4f seconds ---" % (time.time() - start_time))
