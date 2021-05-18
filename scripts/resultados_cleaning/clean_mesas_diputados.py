"""
Genera la base de datos RM_diputados
    Contiene datos sobre los lugares de votación y sus resultados en las elecciones de diputados de la Region Metropolitana.
"""

import csv
import os
from operator import itemgetter

PROBABILIDAD = 0.16

CANDIDATOS = [
    "MARCELA SABAT FERNANDEZ",
    "GIORGIO JACKSON DRAGO",
    "SEBASTIAN TORREALBA ALVARADO",
    "JORGE ALESSAMDRI VERGARA",
    "LUCIANO CRUZ-COKE CARVALLO",
    "NATALIA CASTILLO MUÑOZ",
    "GONZALO WINTER ETCHEBERRY",
    "MAYA FERNANDEZ ALLENDE"
    ]

header = [
    "Región",
    "Provincia"
    "Circ. Senatorial",
    "Distrito",
    "Comuna",
    "Circ. Electoral",
    "Local",
    "Nro. Mesa",
    "Tipo Mesa",
    "Mesas Fusionadas",
    "Electores",
    "Nro. En Voto",
    "Lista",
    "Pacto",
    "Partido",
    "Candidato",
    "Votos TRICEL"
]

header_clean =[
"Región",#0
"Distrito",#3
"Comuna",#4
"Local",#6
"Nro. Mesa",#7
"Mesas Fusionadas",#9
"Electores",#10
"Nro. En Voto",#11
"Lista",#12
"Partido",#14
"Candidato",#15
"Votos TRICEL",#16
]

root = os.path.abspath("../")
print("ROOT: ",root)

mesa_read = csv.reader(open( root + "/Big-Sister/databases/IN/servel/mesa_diputados.csv"), delimiter = ';')
clean_read = csv.reader(open( root + "/Big-Sister/databases/OUT/servel/clean_mesa_diputados.csv"))

def rango():
    with open(root + "/Big-Sister/databases/OUT/servel/clean_probabilidad_mesas.csv", 'w', newline='') as clean_proba:
        writer = csv.writer(clean_proba)
        writer.writerow(header_clean)
        for row in clean_read:
            if row[0] != "Región": 
                if int(row[11]) / int(row[6]) >= PROBABILIDAD:
                    #print(row)
                    writer.writerow(row)

rango()

def formatear():
    with open(root + "/Big-Sister/databases/OUT/servel/clean_mesa_diputados.csv", 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(mesa_read)

        for row in mesa_read:
            for item in row:
                if item in CANDIDATOS:
                    #if int(row[16])/int(row[10]) >= 0.3:
                    row_clean = [row[0], row[3], row[4], row[6], row[7], row[9], row[10], row[11], row[12], row[14], row[15], row[16]]
                    writer.writerow(row_clean)
    rango()

#formatear()

