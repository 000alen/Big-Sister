"""
Genera la base de datos RM_diputados
    Contiene datos sobre los lugares de votación y sus resultados en las elecciones de diputados de la Region Metropolitana.
"""

from csv import reader, writer
from pathlib import Path

print("Generando RM_diputados")

root = Path("../databases/IN/servel/")
out = Path("../databases/OUT/servel/")

print(f"root: {root}")
print(f"out: {out}")

# candidatos = [
#     "MARCELA SABAT FERNANDEZ",
#     "GIORGIO JACKSON DRAGO",
#     "SEBASTIAN TORREALBA ALVARADO",
#     "JORGE ALESSAMDRI VERGARA",
#     "LUCIANO CRUZ-COKE CARVALLO",
#     "NATALIA CASTILLO MUÑOZ",
#     "GONZALO WINTER ETCHEBERRY",
#     "MAYA FERNANDEZ ALLENDE"
# ]

header = [
    "Region",
    "Provincia",
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

tables = {
    "clean_mesa_diputados": [
        "Distrito",
        "Comuna",
        "Local",
        "Nro. Mesa",
        "Tipo Mesa",
        "Electores",
        "Candidato",
        "Votos TRICEL"
    ]
}

mesa_diputados = reader(open(root / "mesa_diputados.csv"))

for table_name, table_header in tables.items():
    print(f"Tabla actual: {table_name}")

    table = writer(open(out / (table_name + ".csv"), "w", newline=""))
    # table.writerow(table_header)

    for row in mesa_diputados:
        row_information = {header[i]: row[i] for i in range(len(row))}
        table.writerow(row_information[key] for key in table_header)
