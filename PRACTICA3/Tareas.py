from collections import deque

# Datos simulados: (tarea, fallos_antes_de_exito, intentos_iniciales)
datos = [
    ("T1", 1, 0),
    ("T2", 0, 0),
    ("T3", 2, 0),
    ("T4", 1, 0),
    ("T5", 2, 2),
    ("T6", 2, 1),
]

bicola = deque()

# Cargar tareas a la bicola con appendleft (entran por la izquierda)
print("=" * 45)
print("📥 CARGANDO TAREAS A LA BICOLA (appendleft)")
print("=" * 45)
for tarea, fallos, intentos in datos:
    bicola.appendleft((tarea, fallos, intentos))
    print(f"  ➕ appendleft → {tarea} | fallos pendientes: {fallos} | intentos: {intentos}")

print(f"\n  Estado inicial: {list(bicola)}\n")

# Procesar tareas
print("=" * 45)
print("⚙️  PROCESANDO TAREAS (popleft)")
print("=" * 45)

turno = 1
while bicola:
    # Sacar tarea por la izquierda
    tarea, fallos, intentos = bicola.popleft()
    print(f"\n[Turno {turno}] popleft ← Procesando: {tarea} | fallos restantes: {fallos} | intentos realizados: {intentos}")

    intentos += 1  # Se realizó un intento

    if fallos > 0:
        # Todavía falla → vuelve al final (append por la derecha)
        fallos -= 1
        bicola.append((tarea, fallos, intentos))
        print(f"  ❌ {tarea} FALLÓ → append al final | fallos restantes: {fallos} | intentos: {intentos}")
    else:
        # Completada → sale del sistema
        print(f"  ✅ {tarea} COMPLETADA y eliminada del sistema (intentos totales: {intentos})")

    print(f"  Bicola actual: {[t[0] for t in bicola]}")
    turno += 1