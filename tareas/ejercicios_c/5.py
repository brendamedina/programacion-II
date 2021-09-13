'''Crea una función que reciba una lista de números
y solo regrese los números pares'''

x = [1,2,3,4,5,6,7,8,9,10]

def regresar_pares():
    for i in x:
        if i % 2 == 0:
            print (i)
           

regresar_pares()
