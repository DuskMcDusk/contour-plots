from math import asin, degrees, radians, sin


testPath = "Data/Tests/test.txt"
expectedPath = "Data/Tests/expected.txt"
testData = []

def convertX(value):
    M = asin((1.54/0.413) * (sin(radians(value))/2))
    return degrees(2*M)

def convertY(value, max):
    return value / max



with open(testPath) as f:
    file_contents = f.read()
    records = file_contents.split("\n")
    entries = []
    for row in records:
        columns = row.split()
        entries.append((float(columns[0]), float(columns[1])))
    print("entries\n", entries)
    for entry in entries:
        xColumn = convertX(entry[0])
        testData.append(xColumn)    
    print("\nDATA:\n",testData)