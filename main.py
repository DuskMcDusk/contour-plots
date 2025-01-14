
import os
from conversion import convertData, convertX, convertY, getColumValues
from parser import parseData, saveAsCsv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import csv
from datetime import datetime
from plot import plotMeasurementsTemperature




folder_path = "Data/inputs/"
csv_path = "Data/csv/"
files = [f for f in os.listdir(folder_path) if "cooling" in f]
measurments = []

for file_name in files:
    source_path = os.path.join(folder_path,file_name)
    data, temperature = parseData(source_path)
    converted_data = convertData(data)

    detination_path = os.path.join(csv_path, file_name.split(".")[0] + ".csv")
    saveAsCsv(source_path, detination_path, converted_data)

    angles = getColumValues(converted_data, 0)
    intensities = getColumValues(converted_data, 1)
    measurments.append({
        "angles": angles, 
        "intensities": intensities,
        "temperature": temperature
    })
# add parameter reverse = True if needed
measurments = sorted(measurments, key=lambda m: m["temperature"])
plotMeasurementsTemperature(measurments)
