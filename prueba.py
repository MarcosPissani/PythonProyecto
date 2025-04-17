import datetime
import csv

with open ("dataSetIndividual.txt","r") as dataSetIndividual:
    data = csv.DictReader(dataSetIndividual,delimiter=";")
    datos = list(data)
    for line in datos:
        fecha = line["CH05"]
        año=fecha[6:10]
        print(año)