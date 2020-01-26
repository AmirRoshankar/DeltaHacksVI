import math
import re

# for the dict key, if key not in the dict, try flipping the order of the states

statesFile = open("states.text", "r")
statesCoords = statesFile.readlines()
states = []

for row in statesCoords:
    row.strip("\n")
    states.append(row.split("\t"))

for i in range(len(statesCoords)):
    for j in range(2):
        states[i][j] = float(states[i][j])

distances = {{}}

for statePair in states:

    lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)

    R = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    phiDelta = math.radians(lat2 - lat1)
    lambdaDelta = math.radians(lon2 - lon1)

    a = math.sin(phiDelta/2) * math.sin(phiDelta/2) + math.cos(phi1) * math.cos(phi2) * math.sin(lambdaDelta/2) * math.sin(lambdaDelta/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c

    print(d)