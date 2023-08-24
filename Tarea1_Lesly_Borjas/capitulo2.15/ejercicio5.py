"""
Ejercicio 5: Escribe un programa que le pida al usuario una temperatura en grados Celsius, 
la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

"""

# función que convierte grados Celsius a grados Fahrenheit
def conversion(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def main():
    # Solicitar al usuario la temperatura en grados Celsius
    celsius = float(input("Ingrese la temperatura en grados Celsius:  "))
    print(' \n')

    # Llamada a la función para realizar la conversión
    fahrenheit = conversion(celsius)

    # Imprime los resultado

    print(f"{fahrenheit}  grados Fahrenheit es equivalente a  {celsius}  grados Celsius que fueron ingresados. ")

# Llamar a la función principal main s
if __name__ == "__main__":
    main()
