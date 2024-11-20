# Matriz para almacenar las cuentas de los usuarios: [número_cuenta, nombre, saldo, pin, historial]
cuentas = [
    ['1234', 'Eduardo', 2000, '1010', []],
    ['5678', 'Ana', 500, '2020', []],
    ['91011', 'Alexander', 750, '3030', []]
]
# Arreglos para almacenar los retiros y depósitos de todas las cuentas
retiros = []  # Registrar retiros globalmente
depositos = []  # Registrar depósitos globalmente

# Función para buscar una cuenta usando búsqueda lineal
def buscar_cuenta(numero_cuenta):
    for cuenta in cuentas:
        if cuenta[0] == numero_cuenta:
            return cuenta
    return None

# Función para validar si la cuenta y el PIN son correctos
def validar_cuenta(numero_cuenta, pin):
    cuenta = buscar_cuenta(numero_cuenta)
    if cuenta and cuenta[3] == pin:
        return True
    return False

# Función para mostrar el saldo
def mostrar_saldo(numero_cuenta):
    cuenta = buscar_cuenta(numero_cuenta)
    saldo = cuenta[2]
    print(f"Tu saldo actual es: ${saldo:.2f}")

# Función para retirar dinero
def retirar_dinero(numero_cuenta, monto):
    cuenta = buscar_cuenta(numero_cuenta)
    saldo_actual = cuenta[2]
    if monto > saldo_actual:
        print(f"No puedes retirar ${monto:.2f}.No tienes suficiente saldo para realizar el retiro. Tu saldo actual es ${saldo_actual:.2f}.")
    else:
        cuenta[2] -= monto
        detalle = f"Retiro realizado: -${monto:.2f} | Nuevo saldo: ${cuenta[2]:.2f}"
        cuenta[4].append(detalle)  # Agregar al historial de la cuenta
        retiros.append([numero_cuenta, monto, detalle])  # Registrar globalmente
        print(detalle)

# Función para depositar dinero
def depositar_dinero(numero_cuenta, monto):
    cuenta = buscar_cuenta(numero_cuenta)
    cuenta[2] += monto
    detalle = f"Depósito realizado: +${monto:.2f} | Nuevo saldo: ${cuenta[2]:.2f}"
    cuenta[4].append(detalle)  # Agregar al historial de la cuenta
    depositos.append([numero_cuenta, monto, detalle])  # Registrar globalmente
    print(detalle)

# Función para mostrar el historial de transacciones
def mostrar_historial(numero_cuenta):
    cuenta = buscar_cuenta(numero_cuenta)
    print("\nHistorial de transacciones:")
    if not cuenta[4]:
        print("No hay transacciones registradas.")
    else:
        for transaccion in cuenta[4]:
            print(transaccion)

# Función para mostrar todos los retiros realizados
def mostrar_retiros():
    print("\nRetiros realizados:")
    if not retiros:
        print("No hay retiros registrados.")
    else:
        for retiro in retiros:
            print(f"Número de cuenta: {retiro[0]}, Monto: ${retiro[1]:.2f}, Detalle: {retiro[2]}")

# Función para mostrar todos los depósitos realizados
def mostrar_depositos():
    print("\nDepósitos realizados:")
    if not depositos:
        print("No hay depósitos registrados.")
    else:
        for deposito in depositos:
            print(f"Número de cuenta: {deposito[0]}, Monto: ${deposito[1]:.2f}, Detalle: {deposito[2]}")

# Función Merge Sort para ordenar transacciones por monto
def merge_sort(arr, indice):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, indice)
        merge_sort(R, indice)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][indice] < R[j][indice]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Función para ordenar y mostrar retiros por monto
def ordenar_retiros_por_monto():
    merge_sort(retiros, 1)  # Ordenar por el índice 1 (monto)
    print("\nRetiros ordenados por monto:")
    mostrar_retiros()

# Función para ordenar y mostrar depósitos por monto
def ordenar_depositos_por_monto():
    merge_sort(depositos, 1)  # Ordenar por el índice 1 (monto)
    print("\nDepósitos ordenados por monto:")
    mostrar_depositos()

# Función principal del cajero
def cajero():
    numero_cuenta = input("Por favor, ingresa tu número de cuenta: ")
    pin = input("Por favor, ingresa tu PIN: ")

    if validar_cuenta(numero_cuenta, pin):
        cuenta = buscar_cuenta(numero_cuenta)
        print(f"Bienvenido/a {cuenta[1]}")
        while True:
            print("\n¿Qué te gustaría hacer?")
            print("1. Consultar saldo")
            print("2. Retirar dinero")
            print("3. Depositar dinero")
            print("4. Ver historial de transacciones")
            print("5. Ver todos los retiros")
            print("6. Ver todos los depósitos")
            print("7. Ordenar retiros por monto")
            print("8. Ordenar depósitos por monto")
            print("9. Cerrar sesión")

            opcion = input("Elige una opción (1,2,3,4,5,6,7,8,9): ")

            if opcion == '1':
                mostrar_saldo(numero_cuenta)
            elif opcion == '2':
                monto = float(input("¿Cuánto deseas retirar?: "))
                retirar_dinero(numero_cuenta, monto)
            elif opcion == '3':
                monto = float(input("¿Cuánto deseas depositar?: "))
                depositar_dinero(numero_cuenta, monto)
            elif opcion == '4':
                mostrar_historial(numero_cuenta)
            elif opcion == '5':
                mostrar_retiros()
            elif opcion == '6':
                mostrar_depositos()
            elif opcion == '7':
                print("Gracias por usar el cajero automático. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
    else:
        print("Número de cuenta o PIN incorrectos.")

# Ejecutar el cajero automático
cajero()