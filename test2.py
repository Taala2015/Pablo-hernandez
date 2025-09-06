print("Escribir un programa que determine si una persona tiene la edad")
print("suficiente para votar y si esta inscrita en el cne")

edad = int(input("ingrese su edad"))

inscrito = input("¿Estas inscrito en el cne? (si/no)").lower()


if edad >=18 and inscrito == "si":
    print("Usted tiene la edad suficiente para votar y esta inscrito en el cne")
else:
    print("Usted no cumple con los requisitod para votar.")