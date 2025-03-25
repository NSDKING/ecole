semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

for jour in semaine:
    print(jour)

print("\nJours du week-end:")

index = 5   
while index < len(semaine):
    print(semaine[index])
    index += 1
    