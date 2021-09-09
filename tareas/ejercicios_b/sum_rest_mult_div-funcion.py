
print ("Ingrese un número")
num1 = float(input())
print ("Ingresa uno de los siguientes operadores: +,-,*,/")
operador = input()
print ("Ingrese otro número")
num2 = float(input())


def calcular ():
    suma = num1 + num2
    resta = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    if operador == "+":
        return suma
    if operador == "-":
        return resta
    if operador == "*":
        return mult
    if operador == "/":
        return div
    

print ("resultado:" ,calcular())


    
    
    
    

 




