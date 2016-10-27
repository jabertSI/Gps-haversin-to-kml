from math import *

terre = 6371
# LECTURE DU FICHIER
fichier_ville = 'ville.txt'
with open(fichier_ville, 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]

carnet = [line.split() for line in lines]
# Conversion string to FLoat
for adr in carnet:
    adr[1] = float(adr[1])
    adr[2] = float(adr[2])
    print(adr[0] + ' : latitude = ' + str(adr[1]) + ' : longitude = ' + str(adr[2]) + ': altitude = ' + adr[3] + "m")
# Generateur de couple
for ville1 in carnet:
    for ville2 in carnet:
        if ville1 != ville2:
            # Calcule de la distance.
            # conversion degre en radian
            ville1[1], ville1[2], ville2[1], ville2[2] = map(radians, [ville1[1], ville1[2], ville2[1], ville2[2]])
            lat = ville2[1] - ville1[1]
            lng = ville2[2] - ville1[2]
            d = sin(lat * 0.5) ** 2 + cos(ville1[1]) * cos(ville2[1]) * sin(lng * 0.5) ** 2
            h = 2 * asin(sqrt(d))
            distance = h * terre
            print(ville1[0], ville2[0], ":", ceil(distance), "km")  # 90 couple possible
