import pandas as pd
import csv

df = pd.read_excel('ALA Load Templates - Item and Inventory - North Pine (Rotating - Updated).xlsx','Assets').fillna(int('0'))
material_locations = []
length = len(df.iloc[:,0])
for row in range(0,length):
    locations = ""
    for ind, value in enumerate(df.iloc[row,:]):
        if value > 0:
            locations = locations + str(df.columns[ind]) + " | "
    material_locations.append(locations)

with open('material_locations.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for string in material_locations:
        csv_writer.writerow([string])

