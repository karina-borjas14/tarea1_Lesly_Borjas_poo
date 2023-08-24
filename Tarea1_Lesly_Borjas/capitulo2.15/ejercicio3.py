"""

Ejercicio 3: Escribe un programa para pedirle al usuario el número de
horas y la tarifa por hora para calcular el salario bruto.

Introduzca Horas: 35
Introduzca Tarifa: 2.75
Salario: 96.25

Por ahora no es necesario preocuparse de que nuestro salario tenga exactamente
dos dígitos después del punto decimal. Si quieres, puedes probar la función interna
de Python round para redondear de forma adecuada el salario resultante a dos
dígitos decimales.

"""

horas = float(input('introduzca horas  trabajadas: '))
tarifa = float(input('intrduzca su tarifa: ')) 

print(f'Su Salario:  {horas*tarifa}')
