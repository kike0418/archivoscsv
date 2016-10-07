import csv
    
with open ('prueba.csv','a') as file:
    dat = csv.writer(file, delimiter=",")
    dat.writerow(['Charles Darwin','charles@correo.com'])

    
with open ('prueba.csv','r') as file:
    data = csv.reader(file, delimiter=',')
    for line in data:
        print line