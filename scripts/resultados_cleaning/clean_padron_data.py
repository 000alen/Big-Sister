import csv
import os

COMUNAS = [
    "ÑUÑOA",
    "MACUL",
    "LA GRANJA",
    "SAN JOAQUIN",
    "PROVIDENCIA",
    "SANTIAGO"
]

archivo = os.path.realpath("../../databases")

csv_reader = csv.reader(open(archivo + "/OUT/servel/elecciones_diputados.csv"))

def formatear():
    with open(archivo + "/OUT/resultados_historicos_diputados.csv", 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)

        for row in csv_reader:
            for item in row:
                if item in COMUNAS:
                    writer.writerow(row)

formatear()
