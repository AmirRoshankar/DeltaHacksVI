import math
import re

# for the dict key, if key not in the dict, try flipping the order of the states

# 1. open and read state coordinates
statesFile = open("states.text", "r")
statesCoords = statesFile.readlines()
states = []

# 2. split each line into substrings of state abbreviation, latitude, longitude
for row in statesCoords:
    row.strip("\n")
    states.append(row.split("\t"))

# 3. convert coordinates into floats for distance calculation below in step 6
for i in range(len(states)):
    for j in range(1,3):
        states[i][j] = float(states[i][j])

# 4. initialize distances nested dictionary with first state nested as a dictionary
distances = {states[0][0]: {}}

# 5. initialize first dimension of distances (first states' distance dictionary)
for i in range(len(states)):
    distances[states[i][0]] = {}

# 6. calculate distances and update secondary dictionaries
for i in range(len(states)):
    for j in range(len(states)):
        for k in range(3):
            R = 6371000
            phi1 = math.radians(states[i][1])
            phi2 = math.radians(states[j][1])
            phiDelta = math.radians(states[j][1] - states[i][1])
            lambdaDelta = math.radians(states[j][2] - states[i][2])

            a = math.sin(phiDelta/2) * math.sin(phiDelta/2) + math.cos(phi1) * math.cos(phi2) * math.sin(lambdaDelta/2) * math.sin(lambdaDelta/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = R * c
            
            distanceForCurrentState = {states[j][0]: d}

            distances[states[i][0]].update(distanceForCurrentState)

print(distances["ND"]["CO"])