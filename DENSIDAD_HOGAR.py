import csv

with open("dataSetHogar.txt","r") as dataSetHogar:
    data = csv.DictReader(dataSetHogar,delimiter=";")
    datos = list(data)
    nuevo_titulo = data.fieldnames + ["DENSIDAD_HOGAR"]

with open("dataSetHogar.txt","w") as dataSetHogar:
    data = csv.DictWriter(dataSetHogar,fieldnames=nuevo_titulo,delimiter=";")
    data.writeheader()

    for file in datos:
        persona = int(file ["IX_Tot"])
        habitacion= int ((file["II1"]))
        personas_x_habitacion = persona / habitacion
        if(personas_x_habitacion < 1):
            file["DENSIDAD_HOGAR"] = "Bajo"
        else:
            if(personas_x_habitacion > 2):
                file["DENSIDAD_HOGAR"]= "Alto"
            else:
                file["DENSIDAD_HOGAR"]= "Medio"
        data.writerow(file)
