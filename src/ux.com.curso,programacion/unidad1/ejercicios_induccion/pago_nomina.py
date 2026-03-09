# Ejercicio de induccion: pago de nomina

numero_horas = float(input("ingrese el numero de horas tranbajadas: "))
tarifa_hora = float(input)("ingrese la tarifa por hora: ")
nombre_empleado = input("ingrese el nombre del empleado ")

# Las horas superiores a 35 se pagan como extras
if numero_horas > 35 :
    horas_extra = numero_horas - 35
    pago_bruto = (35 * tarifa_hora) + (horas_extra * tarifa_hora * 1.5)
else:
    pago_bruto = numero_horas * tarifa_hora

    #calcular impuesto
    if pago_bruto <=2000:
        impuesto = 0
    elif pago_bruto <= 2200:
        impuesto = (pago_bruto - 2000)  * 0.20
    else:
        impuesto = (pago_bruto - 2200) * 0.30 + 220 * 0.20

        pago_neto = pago_bruto - impuesto

        #mostrar resultados
        print(f"empleado: {nombre_empleado}")
        print(f"pago bruto: ${pago_bruto: .2f}")
        print(f"impuesto: ${impuesto: .2f}")
        print(f"pago neto: ${pago_neto: .2f}")




