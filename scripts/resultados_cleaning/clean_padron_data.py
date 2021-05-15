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

root = os.path.abspath("../")

# "/Big-Sister/databases/OUT/servel/resultados_historicos_diputados.csv"

db_historico = open(root + "/Big-Sister/databases/OUT/servel/clean_diputados_historico.csv", "w")

db_historico.close()