import csv

with open("dataSetIndividual.txt","r") as dataSetIndividual :
    data = csv.DictReader(dataSetIndividual,delimiter=";")
    datos = list(data)
    titulo_nuevo = data.fieldnames + ["NIVEL_ED_str"]

with open("dataSetIndividual.txt","w") as dataSetIndividual:
    data = csv.DictWriter(dataSetIndividual,fieldnames=titulo_nuevo,delimiter=";")
    data.writeheader()
    for fila in datos:
        match fila["NIVEL_ED"] :
            case "1":
                fila["NIVEL_ED_str"]= "Primario incompleto"
            case "2":
                fila["NIVEL_ED_str"]= "Primario completo"
            case "3":
                fila["NIVEL_ED_str"]= "Secundario incompleto"
            case "4":
                fila["NIVEL_ED_str"]= "Secundario completo"
            case "5":
                fila["NIVEL_ED_str"]="Superior o universitario"
            case "6":
                fila["NIVEL_ED_str"]="Superior o universitario"
            case "7":
                fila["NIVEL_ED_str"]= "Sin información"
            case "9":
                fila["NIVEL_ED_str"]= "Sin información"
        data.writerow(fila)