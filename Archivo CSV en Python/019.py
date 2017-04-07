import csv

doc = open("archivoW.csv", "w")

doc_csv_w = csv.writer(doc)

lista = ["Pedro", 99836]

doc_csv_w.writerow(lista)

doc.close()