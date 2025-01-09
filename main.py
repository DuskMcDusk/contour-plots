

from conversion import convertX
from parser import parseData

data = parseData("test_input.xyz")
max = float("-inf")
for entry in data:
    if (entry[1] > max):
        max = entry[1]

print(max)