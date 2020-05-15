##menu
totallechevendida=int(0)
totalhuevovendido=int(0)
totalsabritavendida=int(0)
totalcocavendida=int(0)
totalg1=float(0)
totalg2=float(0)
totalg3=float(0)
totalg4=float(0)
producto=int(0)
seleccion=int(0)
leche=int(100)
huevo=int(100)
sabrita=int(100)
coca=int(100)
plitros=float(0)
phuevopza=float(0)
psabrita=float(0)
pcoca=float(0)
total=float(0)
totalp=int(0)
litros=int(0)
huevopza=int(0)
sabritapza=int(0)
litrosc=int(0)
n=0
print("Selecciona del Menú lo que quieras comprar")
print("\n")
print("1 leche")
print("2 huevo")
print("3 sabritas")
print("4 coca")

cobro=input("desea cobrar?(si/no): ")

while (cobro == "si"):

    seleccion=input("selecciona el producto a llevar : ")

    if (seleccion == "1"):
        litros=int(input("cuantos leche llevará(litros no medios)?: "))
        if (leche>0):
            leche=leche-litros
            totallechevendida=totallechevendida+litros
            totalg1=totalg1+(litros*20)
            plitros=(litros*20)
        else:
            print("producto agotado")

    elif (seleccion =="2"):
        huevopza=int(input("Cuanto huevo llevará?: "))
        if (huevo>0):
            huevo=huevo-huevopza
            totalhuevovendido=totalhuevovendido+huevopza
            totalg2=totalg2+(huevopza*18.5)
            phuevopza=(huevopza*18.5)
        else:
            print("producto agotado")
    elif (seleccion=="3"):
        sabritapza=int(input("Cuantas sabritas llevará?: "))
        if (sabrita>0):
            sabrita=sabrita-sabritapza
            totalsabritavendida=totalsabritavendida+sabritapza
            totalg3=totalg3+(sabritapza*12.5)
            psabrita=(sabritapza*12.5)
        else:
            print("producto agotado")
    elif (seleccion=="4"):
        litrosc=int(input("Cuanta coca llevará?(litros no medios):"))
        if(coca>0):
            coca=coca-litrosc
            totalcocavendida=totalcocavendida+litrosc
            totalg4=totalg4+(litrosc*25)
            pcoca=(litrosc*25)
        else:
            print("producto agotado")
    else:
        print("producto erróneo o inexistente")
        print("\n")
    totalac=float(plitros+phuevopza+psabrita+pcoca)
    seguir=input("desea seguir comprando?: ")
    print("\n")
    if (seguir=="si"):

        total=total+totalac
    else:
            total=totalac
            totalp=int((litros+huevopza+sabritapza+litrosc))
            print("usted compro",litros, "litros de leche,",huevopza, "piezas de huevo,",sabritapza,"piezas de sabritas,",litrosc,"de litros de coca")
            print("usted lleva",totalp," productos en su carrito")
            print("el total de su compra es: ", total)
            print("\n")
            print("##########\\PRODUCTO RESTANTE//##########")
            print("QUEDAN",leche,"LITROS DE LECHE EN LA TIENDA")
            if (leche==50):
                print("LECHE A LA MITAD DE SU EXISTENCIA")
            elif (leche==25):
                print("PRODUCTO AGOTANDOSE")
            elif (leche==10):
                print("PRODUCTO ESCASO")
            elif (leche==0):
                print("PRODUCTO AGOTADO")
            print("QUEDAN",huevo,"PIEZAS DE HUEVO EN LA TIENDA")
            if (huevo==50):
                print("LECHE A LA MITAD DE SU EXISTENCIA")
            elif (huevo==25):
                print("PRODUCTO AGOTANDOSE")
            elif (huevo==10):
                print("PRODUCTO ESCASO")
            elif (huevo==0):
                print("PRODUCTO AGOTADO")
            print("QUEDAN",sabrita,"PIEZAS DE SABRITAS EN LA TIENDA")
            if (sabrita==50):
                print("LECHE A LA MITAD DE SU EXISTENCIA")
            elif (sabrita==25):
                print("PRODUCTO AGOTANDOSE")
            elif (sabrita==10):
                print("PRODUCTO ESCASO")
            elif (sabrita==0):
                print("PRODUCTO AGOTADO")
            print("QUEDAN",coca," LITROS DE COCA EN LA TIENDA")
            if (coca==50):
                print("LECHE A LA MITAD DE SU EXISTENCIA")
            elif (coca==25):
                print("PRODUCTO AGOTANDOSE")
            elif (coca==10):
                print("PRODUCTO ESCASO")
            elif (coca==0):
                print("PRODUCTO AGOTADO")

    n=n+1
    cobro=input("continuar cobrando?: ")
else:
    totalproductovendido=float((totallechevendida+totalhuevovendido+totalsabritavendida+totalcocavendida))
    totalganancia=float((totalg1+totalg2+totalg3+totalg4))
    print("##########\\CIERRE DE TIENDA//##########")
    print("HUBO",n,"CLIENTES EN EL DIA")
    print("\n")
    print("##########\\CUANTO SE VENDIO DE CADA PRODUCTO Y CUANTO EN CONJUNTO//##########")
    print("SE VENDIERON",totallechevendida,"LITROS DE LECHE EN EL DIA")
    print("\n")
    print("SE VENDIERON",totalhuevovendido,"DE PIEZA DE HUEVO EN EL DIA")
    print("\n")
    print("SE VENDIERON",totalsabritavendida,"DE PIEZA DE SABRITAS EN EL DIA")
    print("\n")
    print("SE VENDIERON",totalcocavendida,"DE LITROS DE COCA EN EL DIA")
    print("\n")
    print("SE VENDIO UN TOTAL DE",totalproductovendido,"PRODUCTOS EN EL DIA")
    print("\n")
    print("##########\\CUANTO SE GANÓ DE CADA PRODUCTO Y GANANCIA EN TOTAL//##########")
    print("SE GANÓ, ",totalg1,", EN LA VENTA DE LECHE")
    print("\n")
    print("SE GANÓ, ",totalg2, ", EN LA VENTA DE HUEVO")
    print("\n")
    print("SE GANÓ, ",totalg3, ", EN LA VENTA DE SABRITAS")
    print("\n")
    print("SE GANÓ, ",totalg4,", EN LA VENTA DE COCA")
    print("\n")
    print("SE GANÓ UN TOTAL DE: ",totalganancia,"EN EL DIA EN VENTAS")
    print("\n")
    print("##########\\CUANTO PRODUCTO QUEDA DE CADA UNO//##########")
    print("\n")
    print("QUEDAN " ,leche, " LITROS DE LECHE AL CIERRE")
    print("\n")
    print("\n")
    print("QUEDAN " ,huevo, " PIEZAS DE HUEVO AL CIERRE")
    print("\n")
    print("QUEDAN " ,sabrita, " PIEZAS DE SABRITAS AL CIERRE")
    print("\n")
    print("QUEDAN " ,coca, " LITROS DE COCA AL CIERRE")
    print("\n")
    print("REPORTAR DATOS AL DUEÑO O SI NO BALAZO Y PAL RIO PA")