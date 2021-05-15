import csv
import os
from operator import itemgetter

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
    "Region",
    "Provincia",
    "Circ. Senatorial",
    "Distrito",
    "Comuna",
    "Circ. Electoral",
    "Local"
    "Nro. Mesa",
    "Tipo Mesa",
    "Mesas Fusionadas",
    "Electores",
    "Nro. En Voto",
    "Lista",
    "Pacto",
    "Partido",
    "Candidato",
    "Votos TER"   
]

header_clean =[
    "Region", #0
    "Distrito",#3
    "Comuna",#4
    "Local"#6
    "Nro. Mesa",#7
    "Tipo Mesa",#8
    "Electores",#10
    "Nro. En Voto",#11
    "Candidato",#15
    "Votos TER"#16
]

root = os.path.abspath("../")
print("ROOT: ",root)

csv_reader = csv.reader(open( root + "/Big-Sister/databases/IN/servel/resultados_mesa_diputados.csv"), delimiter = ';')

def formatear():
    with open(root + "/Big-Sister/databases/OUT/servel/elecciones_diputados.csv", 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(header_clean)

        for row in csv_reader:
            for item in row:
                if item in CANDIDATOS:
                    row_clean = [row[0], row[3], row[4], row[6], row[7], row[8], row[9], row[10], row[11], row[15], row[16]]
                    writer.writerow(row_clean)

formatear()










