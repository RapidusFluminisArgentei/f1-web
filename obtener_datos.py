import fastf1
import json
import os
from datetime import datetime, timezone

# Creamos una carpeta para el "Cache" de FastF1
os.makedirs('f1_cache', exist_ok=True)
fastf1.Cache.enable_cache('f1_cache')

print("🏎 Conectando con los servidores oficiales de la F1...")

# Le pedimos a FastF1 el calendario de la temporada 2026
calendario = fastf1.get_event_schedule(2026, include_testing=False)

# Obtenemos la fecha actual EN UTC pura
ahora_utc = datetime.now(timezone.utc)

# 1. Armamos la lista de TODO el calendario
lista_calendario = []
for idx, carrera in calendario.iterrows():
    fecha_dt = carrera['Session5Date']
    
    # Formato ISO para JavaScript
    fecha_iso = fecha_dt.strftime('%Y-%m-%dT%H:%M:%SZ') if hasattr(fecha_dt, 'strftime') else None

    # Forzamos a que la fecha de la carrera tenga zona horaria UTC para comparar de forma segura
    if hasattr(fecha_dt, 'tzinfo') and fecha_dt.tzinfo is not None:
        fecha_carrera_utc = fecha_dt.astimezone(timezone.utc)
    else:
        fecha_carrera_utc = fecha_dt.replace(tzinfo=timezone.utc)

    # Ahora ambas son offset-aware en UTC. Comparación 100% segura.
    ya_paso_resultado = bool(fecha_carrera_utc < ahora_utc)

    lista_calendario.append({
        "ronda": int(carrera['RoundNumber']),
        "nombre_gran_premio": str(carrera['EventName']),
        "pais": str(carrera['Country']),
        "ubicacion": str(carrera['Location']),
        "fecha_iso": fecha_iso,
        "ya_paso": ya_paso_resultado
    })

# 2. Buscamos la próxima carrera (la primera futura)
datos_proxima = None
for elemento in lista_calendario:
    if not elemento["ya_paso"]:
        datos_proxima = {
            "nombre_gran_premio": elemento["nombre_gran_premio"],
            "pais": elemento["pais"],
            "ronda": elemento["ronda"],
            "fecha_iso": elemento["fecha_iso"]
        }
        break  # Frenamos en la primera que encontremos que NO haya pasado

# 3. Estructura final
f1_datos_completos = {
    "proxima_carrera": datos_proxima,
    "calendario_completo": lista_calendario
}

# Guardamos todo en 'datos.json'
with open('datos.json', 'w', encoding='utf-8') as f:
    json.dump(f1_datos_completos, f, ensure_ascii=False, indent=4)

print("\n💾 ¡Archivo 'datos.json' actualizado con toda la temporada 2026!")