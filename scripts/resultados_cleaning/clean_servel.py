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

HEDEARS = [
    "Sexo",
    "Región",
    "Comuna",
    "18-19",
    "20-24",
    "25-29",
    "30-34",
    "35-39",
    "40-44",
    "45-49",
    "50-54",
    "55-59",
    "60-64",
    "65-69",
    "70-74",
    "75-79",
    "80- +",
    "TOTAL"
]
root = os.path.abspath("../")

# "/Big-Sister/databases/OUT/servel/resultados_historicos_diputados.csv"

db_etareo = csv.writer(open(root + "/Big-Sister/databases/OUT/servel/clean_etareo_comunas.csv", "w"))

def limpiar_historico():
    etareo = csv.reader(open(root + "/Big-Sister/databases/IN/servel/etareo_comunas.csv", "r"), delimiter = ';')
    db_etareo.writerow(HEDEARS)

    for row in etareo:
        for item in row:
            if item in COMUNAS:
                db_etareo.writerow(row)

limpiar_historico()