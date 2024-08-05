personas = int(input("personas: "))
while personas > 0:
    #Aqui usamos while para verificar que el programa corra solo si hay más de cero personas
    n = input ("Por favor, introduzca su nombre: ")
    while not n.isalpha():
        print("Intenta otra vez, solo se permiten letras")
    #Aqui le pedimos al usuario su nombre  
    e = int(input( "Por favor, introduzca su edad en años: "))
    #Aqui le pedimos su edad para luego usarla en la formula del IMC
    a = float(input ("Por favor, introduzca su altura en metros: "))
    #Aqui le pedimos altura en metros 
    est = a
    #Aqui especificamos est como altura, esto para usar en la formula de IMC
    m = float (input("Por favor, introduzca su peso en kilogramos: "))
    #Por ultimo pedimo su peso en kgs
    IMC = m / est**2
    #Aqui indicamos la formula de IMC 
    if(e < 18):
        #Aqui condicionamos a que si indico que su edad es menor de 18, diga Usted es menor de edad y vicebersa
        print("Usted es menor de edad")
    else:
        print("Usted es mayor de edad")
        #Aqui da el resultado de la formula de IMC al usuario
    print("IMC: " + str(IMC))
    #indicamos los distintos resultados del IMC
    if IMC >= 0 and  IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99:
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("Obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.99:
        print ("Obesidad media")
    elif IMC >= 40.00:
        print ("Obesidad mórbida")
    #Por ultimo, le ordenamos restar una persona al numero de personas que indico el usuario en la primer pregunta.
    personas = personas -1