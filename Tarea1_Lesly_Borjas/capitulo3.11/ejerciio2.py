
"""
Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
del programa:

Introduzca las Horas: 20
Introduzca la Tarifa por hora: nueve

Error, por favor introduzca un número
Introduzca las Horas: cuarenta
Error, por favor introduzca un número

"""

try:
    horas = int(input('introduzca horas: '))
    tarifa= int(input('introduzca tarifa: '))

    if horas <= 40 :
      print(f' Su salario:  {horas* tarifa}')


    else:
       print(f'Su salario:   {horas*(tarifa*1.5)}')

except:
       print('Error por favor introduzca un numero: ')





