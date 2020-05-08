n=str(input("número: "))
if len(n) == 5:
    print("el número tiene cinco dígitos")
else:
        if len(n) ==4:
            print("el número tiene cuatro dígitos")
        else:
            if len(n) ==3:
                print("el número tiene tres dígitos")
            else:
                if len(n) ==2:
                    print("el número tiene dos dígitos")
                else:
                    if len(n) ==1:
                        print("el número tiene un dígito")
                    else:
                        print("no es un número")