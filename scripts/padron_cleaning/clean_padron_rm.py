import csv
from json import load as json_load, dump as json_dump
from csv import reader as csv_reader, writer as csv_writer
from pathlib import Path

root = Path("../raw_padron_rm/")

out = Path("../databases/DCM/")

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

padron_rm_json = json_load(open(root / "raw_padron_rm.json", encoding="utf-8"))

for padron_identifier, padron_paths in padron_rm_json.items():
    print(f"Current padron: {padron_identifier}")

    for table_name, table_header in tables.items():

        table_name = table_name.format(padron_identifier)
        table = csv_writer(open(out / (table_name + ".csv"), "w", encoding="utf-8", newline=""))
        for padron_path in padron_paths:
            print(f"Current padron path: {padron_path}")

            padron = csv_reader(open(root / padron_path, encoding="utf-8", newline=""), delimiter=";")        
            for padron_row in padron:
                padron_row_information = {header[i]: padron_row[i] for i in range(len(padron_row))}

                table_row = [padron_row_information[key] for key in table_header]
                table_row[0] += f", {table_row[1]}, Region Metropolitana, Chile"

                table.writerow(table_row)
