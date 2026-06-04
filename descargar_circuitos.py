import os
import requests

# Crear carpeta si no existe
os.makedirs("img/circuitos", exist_ok=True)

# Diccionario con nombre de archivo y URL del SVG
circuitos = {
    "albert_park.svg": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Albert_Park_Circuit_2022.svg",
    "shanghai.svg": "https://upload.wikimedia.org/wikipedia/commons/1/14/Shanghai_International_Circuit-2004.svg",
    "suzuka.svg": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Suzuka_circuit_map--2005.svg",
    "miami.svg": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Miami_International_Autodrome_2022_Layout.svg",
    "villeneuve.svg": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Circuit_Gilles_Villeneuve_2002.svg",
    "monaco.svg": "https://upload.wikimedia.org/wikipedia/commons/3/36/Monte_Carlo_Formula_1_track_map.svg",
    "barcelona.svg": "https://upload.wikimedia.org/wikipedia/commons/2/20/Circuit_Catalunya_2023.svg",
    "red_bull_ring.svg": "https://upload.wikimedia.org/wikipedia/commons/1/12/Circuit_Red_Bull_Ring.svg",
    "silverstone.svg": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Silverstone_Circuit_2020.svg",
    "spa.svg": "https://upload.wikimedia.org/wikipedia/commons/5/54/Spa-Francorchamps_of_Formula_1.svg",
    "hungaroring.svg": "https://upload.wikimedia.org/wikipedia/commons/9/91/Hungaroring.svg",
    "zandvoort.svg": "https://upload.wikimedia.org/wikipedia/commons/0/07/Circuit_Zandvoort_2020.svg",
    "monza.svg": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Monza_track_map.svg",
    "baku.svg": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Baku_City_Circuit_F1.svg",
    "marina_bay.svg": "https://upload.wikimedia.org/wikipedia/commons/d/df/Marina_Bay_Street_Circuit_2023.svg",
    "cota.svg": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Austin_circuit.svg",
    "hermanos_rodriguez.svg": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Autodromo_Hermanos_Rodriguez_2015.svg",
    "interlagos.svg": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Circuit_Interlagos.svg",
    "las_vegas.svg": "https://upload.wikimedia.org/wikipedia/commons/8/87/Las_Vegas_Grand_Prix_layout.svg",
    "jeddah.svg": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Jeddah_corniche_circuit_2021.svg",
    "yas_marina.svg": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Yas_Marina_Circuit_2021.svg",
    "imola.svg": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Imola_2009.svg",
    "doha.svg": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Lusail_International_Circuit_layout.svg",
    "londres_expo.svg": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Formula_E_London_ExCeL_Circuit.svg"
}

# Descargar cada archivo
for nombre, url in circuitos.items():
    print(f"Descargando {nombre}...")
    r = requests.get(url)
    if r.status_code == 200:
        with open(f"img/circuitos/{nombre}", "wb") as f:
            f.write(r.content)
    else:
        print(f"Error al descargar {nombre}: {r.status_code}")

print("✅ Descarga completa. Los SVG están en /img/circuitos/")

