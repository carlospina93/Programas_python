nom=input("Ingrese nombre: ")
carrera=input("Nombre carrera: ")
i=1
suma=float(0)
final=float(0)
mayor=0
menor=0

while i<=9:
    calif=float(input("Ingresa calificación: "))
    
    i=i+1     

    suma=suma+calif
        
    final=suma/9

    if calif>=7:
        mayor=mayor+1
    
    else:
        menor=menor+1   


if final>=7:
    print("Aprobado")
else:
    print("Reprobado")

print(nom)
print(carrera)
print(final)
print ("son",mayor,"calificaciones mayores o iguales a 7")
print("son",menor,"calificaciones menores a 7")