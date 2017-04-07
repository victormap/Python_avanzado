import csv

doc = open("archivoW.csv", "r")

doc_csv = csv.reader(doc)

for (nombre, numero) in doc_csv:
    print(nombre, numero)

doc.close()