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

# Obtenemos la fecha y hora actual EN UTC
hoy = datetime.now(timezone.utc)

# 1. Armamos la lista de TODO el calendario
lista_calendario = []
for idx, carrera in calendario.iterrows():
    fecha_dt = carrera['Session5Date']
    
    # Esto guarda la fecha en un formato internacional limpio que JS entiende al toque
    fecha_iso = fecha_dt.strftime('%Y-%m-%dT%H:%M:%SZ') if hasattr(fecha_dt, 'strftime') else None

    # Verificamos si la carrera ya pasó comparando de forma segura
    ya_paso_resultado = bool(fecha_dt.tz_localize('UTC') < hoy) if hasattr(fecha_dt, 'tz_localize') else False

    lista_calendario.append({
        "ronda": int(carrera['RoundNumber']),
        "nombre_gran_premio": str(carrera['EventName']),
        "pais": str(carrera['Country']),
        "ubicacion": str(carrera['Location']),
        "fecha_iso": fecha_iso,        # <-- Agregamos esto
        "ya_paso": ya_paso_resultado   # <-- Arreglamos el bug de las pasadas
    }

# 2. Buscamos la próxima carrera (la primera futura)
carreras_futuras = calendario[calendario['Session5Date'] > hoy]
datos_proxima = None

if not carreras_futuras.empty:
    proxima_carrera = carreras_futuras.iloc[0]
    datos_proxima = {
        "nombre_gran_premio": str(proxima_carrera['EventName']),
        "pais": str(proxima_carrera['Country']),
        "ronda": int(proxima_carrera['RoundNumber']),
        "fecha_iso": proxima_carrera['Session5Date'].strftime('%Y-%m-%dT%H:%M:%SZ') # <-- Cambiado a ISO
    }

# 3. Estructura final con datos agrupados
f1_datos_completos = {
    "proxima_carrera": datos_proxima,
    "calendario_completo": lista_calendario
}

# Guardamos todo en 'datos.json'
with open('datos.json', 'w', encoding='utf-8') as f:
    json.dump(f1_datos_completos, f, ensure_ascii=False, indent=4)

print("\n💾 ¡Archivo 'datos.json' actualizado con toda la temporada 2026!")
