import math

def getDistances():
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

    # 4. initialize outer distances list
    distances = []

    # 5. initialize inner distances lists
    for i in range(len(states)):
        distances.append([])

    # 6. calculate distances and append them to inner lists
    for i in range(len(states)):
        for j in range(len(states)):
            R = 6371000
            phi1 = math.radians(states[i][1])
            phi2 = math.radians(states[j][1])
            phiDelta = math.radians(states[j][1] - states[i][1])
            lambdaDelta = math.radians(states[j][2] - states[i][2])

            a = math.sin(phiDelta/2) * math.sin(phiDelta/2) + math.cos(phi1) * math.cos(phi2) * math.sin(lambdaDelta/2) * math.sin(lambdaDelta/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = R * c

            distances[i].append(d)