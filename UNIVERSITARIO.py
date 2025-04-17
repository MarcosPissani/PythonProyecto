import csv
import datetime

with open ("dataSetIndividual.txt","r") as dataSetIndividual:
    data = csv.DictReader(dataSetIndividual,delimiter=";")
    datos = list(data)
    titulo_nuevo = data.fieldnames + ["UNIVERSITARIO"]

with open ("dataSetIndividual.txt","w") as dataSetIndividual:
    data = csv.DictWriter(dataSetIndividual,fieldnames=titulo_nuevo,delimiter=";")
    data.writeheader()
    for line in datos:
        
        año=int(line["CH05"][6:10])
        edad = 2025 - año
        if(edad < 18):
            line["UNIVERSITARIO"] = "2"
        else:
            if(line["NIVEL_ED"] == "6"):
                line["UNIVERSITARIO"]= "1"
            else:
                line["UNIVERSITARIO"]="0"
        data.writerow(line)
