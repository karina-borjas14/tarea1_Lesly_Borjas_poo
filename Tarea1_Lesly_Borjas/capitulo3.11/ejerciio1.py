
"""
Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.


Introduzca las Horas: 45
Introduzca la Tarifa por hora: 10
Salario: 475.


"""

horas = int(input('introduzca horas: '))
tarifa= int(input('introduzca tarifa: '))

if horas <= 40 :
      print(f' Su salario:  {horas* tarifa}')
      
else:
       print(f'Su salario:   {horas*(tarifa*1.5)}')

