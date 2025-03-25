import random
import csv
import json

La_semaine=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
semestre=[]
for mois in range(6):#Parcours des 6mois
	for semaine in range(4):#Parcours des 4 semaines d'un mois
		Temperatures_de_la_semaine=[]
		for jour in La_semaine:
			temperature= random.randint(10,40)
			Temperatures_de_la_semaine.append(temperature)
		semestre.append(Temperatures_de_la_semaine)#semestre va contenir toutes les semaine sur 6 mois donc chaque élément de semestre represente les temp d'une semaine	
print("Les températures ont bien été definies")
#Ecriture dans un fichier csv
with open('Station_meteo.csv','w',newline='') as file :
    writer=csv.writer(file,delimiter=';')#Ici on a forcé Excel à utiliser le point-virgule comme séparateur de colonnes, sans ca les données devaient etre collées confere google
    writer.writerow(La_semaine)
    for semaine in semestre:
        temperatures=[f"{temp} °C" for temp in semaine]
        writer.writerow(temperatures)	
print("Elles ont été enregistré dans le fichier 'Station_meteo.csv' qui se trouve dans le dossier devoirsinfo2 placé sur le bureau ")
#Ecriture dans le fichier json
with open('Station_meteo.json','w') as f:
	json.dump(semestre,f,indent=4)
print("Elles ont été enregistré dans le fichier 'Station_meteo.json' qui se trouve dans le dossier devoirsinfo2 placé sur le bureau ")
#Calcul de la moyenne :
temp_totale=0
nombre_de_temperatures=0
for semaine in semestre:
	temp_totale=temp_totale+sum(semaine)
	nombre_de_temperatures=nombre_de_temperatures+len(semaine)
moy=temp_totale/nombre_de_temperatures
print(f"La température totale est :{moy:.2f} °C")	