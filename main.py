

from conversion import convertX, convertY
from parser import parseData
import csv

data = parseData("Data/inputs/STF_Ni_cooling_f00001.xye")
max = float("-inf")
for entry in data:
    if (entry[1] > max):
        max = entry[1]
with open("STF_Ni_cooling_f00001.csv", "w", newline='') as file:
    field_names = ["2M°", "Normalized Intensity"]
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    for entry in data:
        try: 
            csv_record = {
                "2M°": convertX(entry[0]), 
                "Normalized Intensity": convertY(entry[1], max)
            }
            writer.writerow(csv_record)
        except:
            print(entry)
            continue