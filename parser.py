def parseData(filePath):
    results = []
    f = open(filePath, "r")
    file_lines = f.readlines()
    f.close()
    for line in file_lines:
        if line.startswith("#"):
            continue
        columns = line.split()
        parsed_columns = [float(columns[0]), float(columns[1])]
        results.append(parsed_columns)
    return results