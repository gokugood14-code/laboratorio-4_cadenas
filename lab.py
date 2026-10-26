print("=" * 50)
print("OPERACIONES CON CADENAS")
print("=" * 50)

texto = "Python es un lenguaje de programación muy popular y fácil de aprender"
print("Texto original:", texto)

subcadena = texto[0:6]
print("\n[a] Subcadena (posiciones 0 a 6):", subcadena)

palabra = "lenguaje"
posicion = texto.find(palabra)
if posicion != -1:
    print(f"[b] La palabra '{palabra}' se encontró en la posición {posicion}")
else:
    print(f"[b] La palabra '{palabra}' no se encontró")


texto_nuevo = texto.replace("popular", "usado")
print("[c] Texto con reemplazo:", texto_nuevo)


partes = texto.split(" ")
print("[d] Texto separado en palabras:", partes)
print("    Cantidad de palabras:", len(partes))

print("\n" + "=" * 50)
print("LISTAS PARALELAS")
print("=" * 50)

nombres = ["Ana", "Luis", "María", "Carlos", "Sofía"]
edades = [20, 22, 19, 25, 21]


def buscar_edad(nombre_buscado):
    """Busca el nombre en la primera lista y devuelve la edad de la segunda."""
    if nombre_buscado in nombres:
        indice = nombres.index(nombre_buscado)
        return edades[indice]
    return None


for n in ["María", "Carlos", "Pedro"]:
    edad = buscar_edad(n)
    if edad is not None:
        print(f"{n} tiene {edad} años")
    else:
        print(f"{n} no está en la lista")


print("\n" + "=" * 50)
print("LISTA DE DICCIONARIOS")
print("=" * 50)

usuarios = [
    {"nombre": "Ana", "email": "ana@gmail.com", "ciudad": "Lima"},
    {"nombre": "Luis", "email": "luis@gmail.com", "ciudad": "Trujillo"},
    {"nombre": "María", "email": "maria@gmail.com", "ciudad": "Lima"},
    {"nombre": "Carlos", "email": "carlos@gmail.com", "ciudad": "Cajamarca"},
    {"nombre": "Sofía", "email": "sofia@gmail.com", "ciudad": "Trujillo"},
]

for u in usuarios:
    print(f"Nombre: {u['nombre']:<8} | Email: {u['email']:<18} | Ciudad: {u['ciudad']}")


print("\n" + "=" * 50)
print("BÚSQUEDA POR CIUDAD")
print("=" * 50)

ciudad_buscada = "Lima"
coincidencias = [u for u in usuarios if ciudad_buscada.lower() in u["ciudad"].lower()]

print(f"Usuarios que viven en {ciudad_buscada}:")
if coincidencias:
    for u in coincidencias:
        print(f" - {u['nombre']} ({u['email']})")
else:
    print(" No hay coincidencias")

print("\n" + "=" * 50)
print("ORDEN ALFABÉTICO")
print("=" * 50)

ordenados = sorted(usuarios, key=lambda u: u["nombre"].lower())
for u in ordenados:
    print(f" - {u['nombre']}")

print("\n" + "=" * 50)
print("VALIDACIÓN")
print("=" * 50)
print("Total de usuarios:", len(usuarios))
print("Nombres ordenados:", [u["nombre"] for u in ordenados])
print("Todas las operaciones se ejecutaron correctamente.")
