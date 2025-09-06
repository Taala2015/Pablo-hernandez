print("CALCULADORA SIMPLE\n")

operacion = input("Elige la operacion que desea realizar (SUMA,RESTA,DIVISION,MULTIPLICACION)")

if operacion == "SUMA":
    numero_1 = float(input("Ingresa el primer numero: "))
    numero_2 = float(input("Ingresa el segundo numero: "))

    resultado = numero_1 + numero_2

    print(f"el resultado de la suma es: ¨{resultado}")

elif operacion == "RESTA":
    numero_3 = float(input("ingresa el primer numero:"))
    numero_4 = float(input("ingreasa el segundo numero:"))

    resultado = numero_3 - numero_4


    print(f"el resultado de la resta es: {resultado}")


elif operacion == "DIVISION":
    numero_5 = float(input("ingresa el primer numero:"))
    numero_6 = float(input("ingreasa el segundo numero:"))

    resultado = numero_5 - numero_6


    print(f"el resultado de la division es: {resultado}")

elif operacion == "MULTIPLICACION":
    numero_7 = float(input("ingresa el primer numero:"))
    numero_8 = float(input("ingreasa el segundo numero:"))

    resultado = numero_7 * numero_8


    print(f"el resultado de la multiplicacion es: {resultado}")
     


    
