import csv

with open("dataSetIndividual.txt","r") as dataSetIndividual:
    data = csv.DictReader(dataSetIndividual,delimiter=";")
    datos= list(data)
    titulo_nuevo = data.fieldnames + ["CONDICION_LABORAL"]

with open ("dataSetIndividual.txt","w") as dataSetIndividual:
    data = csv.DictWriter(dataSetIndividual,fieldnames=titulo_nuevo,delimiter=";")
    data.writeheader()
    for line in datos:
        match line["ESTADO"]:
            case "1":
                if line["CAT_OCUP"] == "1" or line["CAT_OCUP"] =="2":
                    line["CONDICION_LABORAL"] = "Ocupado autonomo"
                else:
                    line["CONDICION_LABORAL"] = "Ocupado dependiente"                
            case "2":
                line["CAT_OCUP"] = "Desocupado"
            case "3":
                line["CAT_OCUP"] = "Inactivo"
            case "4":
                line["CAT_OCUP"] = "Fuera de categoría/sin información"
        data.writerow(line)