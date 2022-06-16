
# input

identificacion=int(input("Digite su identificacion: "))
print("")


# processing

if  identificacion!=0:
     cheque=int(input("Digite el valor del cheque: "))


if cheque !=0:
    print("")
    print("Contando dinero")

else:
    print("error")
    identificacion=int(input("Digite su identificacion: "))
    cheque=int(input("Digite el valor del cheque: "))


while cheque !=0:
    usuarios=0
    moneda=cheque
    billete10000=(moneda-moneda%10000)//10000
    moneda=moneda%10000
    billete2000=(moneda-moneda%2000)//2000
    moneda=moneda%2000
    moneda=(moneda-moneda%100)//100
    moneda=moneda%100
    gasto= (moneda+ billete2000 + billete10000)
    usuarios=usuarios +1 
    cheque=0
   

   

    
# ouput 
print("")
print("Cantidad de monedas de 100 :", moneda)
print("")
print("Cantiddad de Billetes de 10000:",billete10000)
print("")
print("Cantidad de Billetes de 2000:",billete2000)
print("")


# input

identificacion=int(input("Digite su identificacion: "))
print("")


# processing

if  identificacion!=0:
     cheque=int(input("Digite el valor del cheque: "))


if cheque !=0:
    print("")
    print("Contando dinero")

else:
    print("error")
    identificacion=int(input("Digite su identificacion: "))
    cheque=int(input("Digite el valor del cheque: "))


while cheque !=0:
    usuarios=0
    moneda=cheque
    billete10000=(moneda-moneda%10000)//10000
    moneda=moneda%10000
    billete2000=(moneda-moneda%2000)//2000
    moneda=moneda%2000
    moneda=(moneda-moneda%100)//100
    moneda=moneda%100
    gasto= (moneda+ billete2000 + billete10000)
    usuarios=usuarios +1 
    cheque=0
   

# ouput 
print("")
print("Cantidad de monedas de 100 :", moneda)
print("")
print("Cantiddad de Billetes de 10000:",billete10000)
print("")
print("Cantidad de Billetes de 2000:",billete2000)
print("")
print("Los cheques descambiados fueron: ",usuarios)
print("")

    

    