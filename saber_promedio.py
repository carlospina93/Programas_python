nom=input("Ingresa nombre de Alumno: ")
carrera=input("Ingresa Carrera: ")
i=1
suma=float(0)
final=float(0)
while i<=5:
    calif=float(input("Ingresa calificación: "))
    i=i+1
    suma=suma+calif
    
    final=suma/5

if final == 10:
        print(nom)
        print(carrera)
        print("A")
        print(final)
        
else:
        if final>=9 and final<=10:
             print("B")
        else:
                if final<9 and final>=8:
                    print("C")
                else:
                        if final<8 and final>=7:
                            print("D")
                        else:
                            if final<7 and final>=6:
                                print("E")
                            else:
                                if final<6:
                                    print("F")
                                else:
                                    print("Promedio erróneo.")
        
    
    
    
        print(final)
        print(nom)
        print(carrera)
