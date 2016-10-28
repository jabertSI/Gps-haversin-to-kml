from math import radians, cos, sin, atan2, sqrt, ceil


terre = 6371
# LECTURE DU FICHIER
fichier_ville = 'ville.txt'
with open(fichier_ville, 'r') as f:
    # Creation liste de liste
    lines = [line.strip('\n') for line in f.readlines()]


carnet = [line.split() for line in lines] #Decoupage de la chaine de caractere
# Conversion string to FLoat
print("INFORMATION VILLE :")
for adr in carnet:
    adr[1] = float(adr[1])
    adr[2] = float(adr[2])
    print(adr[0] + ' : latitude = ' + str(adr[1]) + ' : longitude = ' + str(adr[2]) + ': altitude = ' + adr[3] + "m")

for ville1 in carnet:
    ville1[1], ville1[2] = map(radians, [ville1[1], ville1[2]]) # conversion degre en radian

distances = []

# Generateur de couple
print("DISTANCE ENTRE LES VILLES :")
for ville1 in carnet:
    for ville2 in carnet:
        if ville1 != ville2:
            # Calcule de la distance.
            lat = ville2[1] - ville1[1] #  delta latitude
            lng = ville2[2] - ville1[2] # delta longitude
            # formule haversine
            d = sin(lat * 0.5) ** 2 + cos(ville1[1]) * cos(ville2[1]) * sin(lng * 0.5) ** 2
            h = 2 * atan2(sqrt(d),sqrt(1-d))
            distance = h * terre
            print("La distance entre", ville1[0],"et", ville2[0], "est de", ceil(distance), "km")  # 90 couple possible
# Fin partie 1
# Debut partie 2
            distances.append([ville1[0], ville2[0], ceil(distance)]) # Création de la list afin de stock les couples avec leurs distance antre elles
distances.sort(key=lambda x:x[2]) # FOnction qui dit que le tri se fait sur la key n° 2 donc la distance en km


for dist in distances:
    print("La distance entre", dist[0], "et", dist[1], "est de", ceil(dist[2]), "km") # Affichage super beau 
