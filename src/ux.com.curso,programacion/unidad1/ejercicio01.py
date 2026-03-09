# --- ENTRADA DE DATOS ---
nombre = input("Ingrese el nombre del empleado: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas esta semana: "))
tarifa_hora = float(input("Ingrese el pago por hora: "))

# --- LÓGICA DE HORAS EXTRA ---
if horas_trabajadas > 40:
    horas_normales = 40
    horas_extras = horas_trabajadas - 40
else:
    horas_normales = horas_trabajadas
    horas_extras = 0

pago_bruto = (horas_normales * tarifa_hora) + (horas_extras * tarifa_hora * 2)

# --- NUEVA LÓGICA DE IMPUESTOS ESCALONADOS ---
# Tramo 1: Hasta 2000 -> 0%
# Tramo 2: Los siguientes 220 (de 2001 a 2220) -> 20%
# Tramo 3: El resto (más de 2220) -> 30%

impuesto_total = 0

if pago_bruto > 2000:
    # Calculamos cuánto excede de los 2000 iniciales
    excedente_de_2000 = pago_bruto - 2000
    
    if excedente_de_2000 <= 220:
        # Si el excedente está dentro del segundo tramo
        impuesto_total = excedente_de_2000 * 0.20
    else:
        # Si llega al tercer tramo:
        # 1. Impuesto del segundo tramo completo (220 * 0.20 = 44)
        # 2. Impuesto del 30% sobre lo que sobre de 2220
        impuesto_segundo_tramo = 220 * 0.20
        excedente_de_2220 = pago_bruto - 2220
        impuesto_total = impuesto_segundo_tramo + (excedente_de_2220 * 0.30)
else:
    impuesto_total = 0

pago_neto = pago_bruto - impuesto_total

# --- SALIDA DE RESULTADOS ---
print("-" * 30)
print(f"Recibo de: {nombre}")
print(f"Sueldo Bruto: ${pago_bruto:.2f}")
print(f"Impuestos Totales: ${impuesto_total:.2f}")
print(f"Sueldo Neto a pagar: ${pago_neto:.2f}")
print("-" * 30)