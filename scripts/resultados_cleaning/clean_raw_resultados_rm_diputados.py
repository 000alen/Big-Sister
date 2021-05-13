import csv
import os

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

a = os.path.dirname("../../databases")
print(a)

csv_reader = csv.reader(open("/Users/jp/Documents/Programacion/Python/Big-Sister/databases/IN/servel/Resultados_Mesa_DIPUTADOS.csv"), delimiter = ';')

with open('/Users/jp/Documents/Programacion/Python/Big-Sister/databases/OUT/servel/elecciones_diputados.csv', 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(header)

    #"Region", #0
    #"Distrito",#3
    #"Comuna",#4
    #"Local"#6
    #"Nro. Mesa",#7
    #"Tipo Mesa",#8
    #"Mesas Fusionadas",#9
    #"Electores",#10
    #"Nro. En Voto",#11
    #"Candidato",#15
    #"Votos TER"#16
    
    for i in csv_reader:
        for b in i:
            if b == CANDIDATO:
                outcsv.writelines(i + " ,")











