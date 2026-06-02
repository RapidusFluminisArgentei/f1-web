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
    lista_calendario.append({
        "ronda": int(carrera['RoundNumber']),
        "nombre_gran_premio": str(carrera['EventName']),
        "pais": str(carrera['Country']),
        "ubicacion": str(carrera['Location']),
        "fecha_carrera": str(carrera['Session5Date'].strftime('%d/%m/%Y')) if hasattr(carrera['Session5Date'], 'strftime') else "TBD",
        "hora_carrera": str(carrera['Session5Date'].strftime('%H:%M')) if hasattr(carrera['Session5Date'], 'strftime') else "TBD",
        "ya_paso": bool(carrera['Session5Date'] < hoy) if hasattr(carrera['Session5Date'], 'timezone') else False
    })

# 2. Buscamos la próxima carrera (la primera futura)
carreras_futuras = calendario[calendario['Session5Date'] > hoy]
datos_proxima = None

if not carreras_futuras.empty:
    proxima_carrera = carreras_futuras.iloc[0]
    datos_proxima = {
        "nombre_gran_premio": str(proxima_carrera['EventName']),
        "pais": str(proxima_carrera['Country']),
        "ronda": int(proxima_carrera['RoundNumber']),
        "fecha_carrera": str(proxima_carrera['Session5Date'].strftime('%d/%m/%Y')),
        "hora_carrera": str(proxima_carrera['Session5Date'].strftime('%H:%M'))
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
