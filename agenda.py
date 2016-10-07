import csv
import sys
print "==========Menu============="
print "1. Leer"
print "2. Insertar"
print "3. Salir"


opcion=int(input("Que quieres realizar? "))

if opcion == 1:
    with open ('prueba.csv','r') as file:
        data = csv.reader(file, delimiter=',')
        for line in data:
            print line
if opcion == 2:
    nombre = raw_input("Ingresa el nombre: ")
    email =  raw_input("Ingresa el email: ")
    with open ('prueba.csv','a') as file:
        dat = csv.writer(file, delimiter=",")
        dat.writerow([''+str(nombre),''+str(email)])
if opcion==3:    
    sys.exit(0)