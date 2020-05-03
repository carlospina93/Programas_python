sexo=input("ingresa sexo: ")
edad=input("ingresa edad: ")

if(sexo=="mujer" and edad>="18"):
    print("es mujer y mayor de 18")
elif(sexo=="mujer" and edad<="18"):
    print("es mujer y menor de 18")
elif(sexo=="hombre" and edad>="18"):
     print(" es hombre y mayor a 18")
elif(sexo=="hombre" and edad<="18"):
     print("es hombre y menor a 18")
else:
     print("persona no válida")


