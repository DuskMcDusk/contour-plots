from math import asin, degrees, radians, sin

def convertX(value):
    M = asin((1.54/0.413) * (sin(radians(value))/2))
    return round(degrees(2*M), 5)

def convertY(value, max):
    return float(f"{value / max:.2e}")

def getMaxValue(data):
    max = float("-inf")
    for entry in data:
        if (entry[1] > max):
            max = entry[1]
    return max

def getColumValues(data, index):
    result = []
    for entry in data:
        result.append(entry[index])
    return result

def convertData(data):
    result = []
    max = getMaxValue(data)
    for entry in data:
        try: 
            result.append([convertX(entry[0]), convertY(entry[1], max)])
        except:
            continue
    return result