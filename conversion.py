from math import asin, degrees, radians, sin

def convertX(value):
    M = asin((1.54/0.413) * (sin(radians(value))/2))
    return round(degrees(2*M), 5)

def convertY(value, max):
    return float(f"{value / max:.2e}")