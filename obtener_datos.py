import fastf1
import json
import os
from datetime import datetime, timezone

# Creamos una carpeta para el "Cache" de FastF1
os.makedirs('f1_cache', exist_ok=True)
fastf1.Cache.enable_cache('f1_cache')

print("🏎️ Conectando con los servidores oficiales de la F1...")

# Le pedimos a FastF1 el calendario de la temporada 2026
calendario = fastf1.get_event_schedule(2026, include_testing=False)

# Obtenemos la fecha y hora actual EN UTC para que coincida con FastF1
hoy = datetime.now(timezone.utc)

# Filtramos las carreras cuya fecha de sesión sea mayor (posterior) a hoy
carreras_futuras = calendario[calendario['Session5Date'] > hoy]

if not carreras_futuras.empty:
    # Agarramos la primera de la lista (la más cercana en el tiempo)
    proxima_carrera = carreras_futuras.iloc[0]
    
    # Extraemos los datos limpios
    datos_proxima = {
        "nombre_gran_premio": str(proxima_carrera['EventName']),
        "pais": str(proxima_carrera['Country']),
        "ronda": int(proxima_carrera['RoundNumber']),
        "fecha_carrera": str(proxima_carrera['Session5Date'].strftime('%d/%m/%Y')),
        "hora_carrera": str(proxima_carrera['Session5Date'].strftime('%H:%M'))
    }

    print(f"\n✨ ¡Datos recuperados con éxito!")
    print(f"📌 Próximo evento: {datos_proxima['nombre_gran_premio']} en {datos_proxima['pais']}")

    # Guardamos en el archivito 'datos.json'
    with open('datos.json', 'w', encoding='utf-8') as f:
        json.dump(datos_proxima, f, ensure_ascii=False, indent=4)

    print("\n💾 Archivo 'datos.json' generado correctamente.")
else:
    print("\n🏁 No se encontraron más carreras programadas para el resto de la temporada 2026.")
