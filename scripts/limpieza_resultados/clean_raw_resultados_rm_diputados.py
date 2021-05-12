import csv

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



file = open("../../databases/Resultados_Mesa_DIPUTADOS.xlsx", "r")

for i in file:
    print(i)

file.close()




