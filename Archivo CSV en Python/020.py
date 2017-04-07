import csv

doc = open("archivoW.csv", "w")

doc_csv_w = csv.writer(doc)

lista = [["Pedro", 99836], ["UNO", 1000], ["DOS", 20000], ["TRES", 4000], ["CUATRO", 4000]]

doc_csv_w.writerows(lista)

doc.close()