import csv
#abrimos los asrchivos con los datos
hogar1 =csv.DictReader(open("usu_hogar_T124.txt"),delimiter=";") 
hogar2 =csv.DictReader(open("usu_hogar_T224.txt"),delimiter=";") 
hogar3 =csv.DictReader(open("usu_hogar_T324.txt"),delimiter=";") 
ind1 =csv.DictReader(open("usu_individual_T124.txt"),delimiter=";") 
ind2 =csv.DictReader(open("usu_individual_T224.txt"),delimiter=";") 
ind3 =csv.DictReader(open("usu_individual_T324.txt"),delimiter=";") 

#abrimos los archivos dataset donde vamos a poner los datos
dataSetHogar =(open("dataSetHogar.txt","w",newline="")) 
dataSetIndividual = (open("datasetIndividual.txt","w",newline="")) 

write_hogar = csv.DictWriter(dataSetHogar,fieldnames=hogar1.fieldnames, delimiter=";")

write_hogar.writeheader()

for line in hogar1:
    write_hogar.writerow(line)
for line in hogar2:
    write_hogar.writerow(line)
for line in hogar3:
    write_hogar.writerow(line)


write_ind = csv.DictWriter(dataSetIndividual,fieldnames=ind1.fieldnames, delimiter=";")

write_ind.writeheader()

for line in ind1:
    write_ind.writerow(line)
for line in ind2:
    write_ind.writerow(line)
for line in ind3:
    write_ind.writerow(line)


dataSetHogar.close()
dataSetIndividual.close()

