##pedir edades y el sexo de n personas, seguir contando hasta que se ingrese por teclado "no"
## imprimir cuantas mujeres menores de edad
## imprimir cuantas mujeres mayores de edad
## cuantos hombres menores de edad
## cuantos hombres mayores de edad
## si el sexo es diferente de "masculino" o "femenino" imprimir "sexo erróneo" y terminar programa
## cuando se llegue a 5 hombres mayores de edad imprimir "se han censado 5 hombres hasta el momento" y continuar el programa
## cuando se llegue a 5 mujeres mayores de edad imprimir " se han censado 5 mujeres hasta el momento" y continuar el programa
## imprimir el numero de personas censadas

mmayor=0
mmenor=0
hmayor=0
hmenor=0
suma=0

persona=input("ingresar datos?: ")

while (persona!="no"):
    edad=int(input("ingresar edad: "))
    sexo=input("ingresar sexo (h/m): ")
    if (sexo=="h" or sexo=="m"):
        if(sexo=="h" and edad>=18):
            hmayor+=1
            if (hmayor==5):
                print("se han censado 5 hombres mayores")
        elif(sexo=="m" and edad>=18):
            mmayor+=1
            if(mmayor==5):
                print("se han censado 5 mujeres mayores")
        elif(sexo=="m" and edad<18):
            mmenor+=1
        elif(sexo=="h" and edad<18):
            hmenor+=1
        suma+=1
    else:
        print("ingresa género válido")
        break

res=input("ingresar datos:")

print("Numero de personas censadas:",suma)
print("Hombres mayores",hmayor)
print("Hombres menores",hmenor)
print("Mujeres mayores",mmayor)
print("Mujeres menores",mmenor)
