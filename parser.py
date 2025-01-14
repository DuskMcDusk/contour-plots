import csv
from datetime import datetime
import os
from pathlib import Path

def parseData(filePath):
    results = []
    f = open(filePath, "r")
    file_lines = f.readlines()
    f.close()
    temp = 0
    for line in file_lines:
        if line.startswith("#"):
            tmp = GetTemperature(line)
            if(tmp != 0): temp = tmp
            continue
        columns = line.split()
        parsed_columns = [float(columns[0]), float(columns[1])]
        results.append(parsed_columns)
    return (results, temp)

def GetTemperature(line):
    temp_marker = "<blowerC> = "
    end_marker = " +/-"
    return float(getStringValueBetween(line, temp_marker, end_marker))

def getTime(line):
    time_marker = "Date = "
    end_marker = " Dt"
    value = getStringValueBetween(line, time_marker, end_marker)
    if value == 0: return None
    return datetime.strptime(value, "%Y-%m-%d_%H:%M:%S") 

def getStringValueBetween(line, start, end):
    index = line.find(start)
    if index == -1: return 0
    index += len(start)
    endIndex = line.find(end, index)
    if endIndex == -1: return
    return line[index:endIndex]

def saveAsCsv(dest, converted_data):
    if os.path.exists(dest):
        return
    file = Path(dest)
    file.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", newline='') as file:
        field_names = ["angle", "normalized intensity"]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for entry in converted_data:
            try: 
                csv_record = {
                    "angle": entry[0], 
                    "normalized intensity": entry[1],
                }
                writer.writerow(csv_record)
            except:
                print(entry)
                continue