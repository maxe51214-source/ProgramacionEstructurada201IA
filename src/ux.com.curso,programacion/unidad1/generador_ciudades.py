from faker import Faker
fake = Faker('es_MX')

#1. Declaración de un vector vacío
ciudades_ia =[]

#2. Operación de llenado (Ciclo)
for _ in range(5):
    ciudades_ia.append(fake.city())

#3. Estructura de arreglos (Mostrar resultados)
print("\n--- DATATEST DE CIUDADES GENERADO ---")
for i in range(len(ciudades_ia)):
    print(f"Registro {i+1}: {ciudades_ia[i]}")
