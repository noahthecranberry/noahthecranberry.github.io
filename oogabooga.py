import pandas as pd
import csv

with open('SJCC Player List - Sheet4.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)