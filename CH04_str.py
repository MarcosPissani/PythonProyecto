import csv

with open("datasetIndividual.txt","r",newline='') as dataSetIndividual:
     data = csv.DictReader(dataSetIndividual,delimiter=";")
     datos = list(data)
     titulo = data.fieldnames

titulo_nuevo = titulo + ["CH04_str"]
with open("datasetIndividual.txt","w",newline='') as dataSetIndividual:
     data = csv.DictWriter(dataSetIndividual,fieldnames=titulo_nuevo,delimiter=";")
     data.writeheader()
     for fila in datos :
         match fila["CH04"]:
              case "1":
                   fila["CH04_str"]="Hombre"
              case "2":
                   fila["CH04_str"]="Mujer"
         data.writerow(fila)
