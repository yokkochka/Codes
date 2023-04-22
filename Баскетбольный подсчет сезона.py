games = [40, 50, 10, 23, 15, 16, 35, 31, 26, 39, 24, 8, 15, 20, 40, 33, 26, 19, 14, 12]
goodgames = 0
badgames = 0

for i in games:
    if i>=20:
        goodgames+=1
    else:
        badgames += 1
        
if goodgames>badgames:
    print("Сезон хороший!")
else:
    print("Сезон не удачный, постараемся в следующем!")