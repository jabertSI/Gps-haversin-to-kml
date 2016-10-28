from math import radians, cos, sin, atan2, sqrt, ceil

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

for ville1 in carnet:
    ville1[1], ville1[2] = map(radians, [ville1[1], ville1[2]])

# Generateur de couple
for ville1 in carnet:
    for ville2 in carnet:
        if ville1 != ville2:
            # Calcule de la distance.
            # conversion degre en radian
            lat = ville2[1] - ville1[1]
            lng = ville2[2] - ville1[2]
            d = sin(lat * 0.5) ** 2 + cos(ville1[1]) * cos(ville2[1]) * sin(lng * 0.5) ** 2
            h = 2 * atan2(sqrt(d),sqrt(1-d))
            distance = h * terre
            print("La distance entre", ville1[0],"et", ville2[0], "est de", ceil(distance), "km")  # 90 couple possible
