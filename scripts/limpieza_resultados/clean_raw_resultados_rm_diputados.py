import csv
import os
from pathlib import Path

CANDIDATO = "GIORGIO JACKSON DRAGO"

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

root = Path("../../databases/")

#print(root)

csv_reader = csv.reader(open("/Users/jp/Documents/Programacion/Python/Big-Sister/databases/Resultados_Mesa_DIPUTADOS.csv"), delimiter = ';')

for i in csv_reader:
    for b in i:
        if b == CANDIDATO:
            print(i)









