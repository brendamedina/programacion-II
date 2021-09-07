print ("¿Cuánto pesas?")
p = float(input())
print ("¿Cuánto mides? (en cm)")
a = int(input ())

def calcular_imc():
    imc = p / (a/100)**2
    return imc

print ("Tu imc es:", calcular_imc())

imc = p / (a/100)**2
if imc <= 18.4:
    print ("Tienes un peso bajo")
if imc >= 18.5 and imc <= 24.9:
    print ("Tienes un peso normal")
if imc >= 25 and imc <= 29.9:
    print ("Tienes sobrepeso")
if imc >= 30 and imc <= 34.9:
    print ("Tienes obesidad grado I")
if imc >= 35 and imc <= 39.9: 
    print ("Tienes obesidad grado II")
if imc >= 40:
    print ("Tienes obesidad morbida")

