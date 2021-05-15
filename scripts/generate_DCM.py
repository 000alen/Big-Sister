"""
Genera la base de datos DCM.
    Contiene el Domicilio, la Circunscripción y la Mesa de los votantes de la Region Metropolitana.
"""

from json import load
from csv import reader, writer
from pathlib import Path

print("Generando DCM")

root = Path("../../databases/IN/raw_padron_rm/")
out = Path("../../databases/OUT/DCM/")

print(f"root: {root}")
print(f"out: {out}")

header = [
    "RUT",
    "DV",
    "Proper RUT",
    "Nombre completo",
    "Primer nombre",
    "Segundo nombre",
    "Primer apellido",
    "Segundo apellido",
    "Sexo",
    "Domicilio",
    "Circunscripcion",
    "Local?",
    "Mesa",
    "Pueblo",
]

tables = {
    "DCM_{}": ["Domicilio", "Circunscripcion",  "Mesa"]
}

padron_rm_json = load(open(root / "raw_padron_rm.json", encoding="utf-8"))

for padron_identifier, padron_paths in padron_rm_json.items():
    print(f"Padron actual: {padron_identifier}")

    for table_name, table_header in tables.items():

        table_name = table_name.format(padron_identifier)
        table = writer(open(out / (table_name + ".csv"),
                       "w", encoding="utf-8", newline=""))
        # table.writerow(table_header)
        for padron_path in padron_paths:
            padron = reader(
                open(root / padron_path, encoding="utf-8", newline=""), delimiter=";")
            for padron_row in padron:
                padron_row_information = {
                    header[i]: padron_row[i] for i in range(len(padron_row))}

                table_row = [padron_row_information[key]
                             for key in table_header]
                table_row[0] += f", {table_row[1]}, Region Metropolitana, Chile"

                table.writerow(table_row)
