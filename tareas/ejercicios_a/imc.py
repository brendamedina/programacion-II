altura = 161
peso = 55
imc = peso / (altura/100)**2

print ("Tu imc es: " , imc)

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
