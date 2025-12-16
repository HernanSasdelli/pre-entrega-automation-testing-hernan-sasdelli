import csv
import json
from pathlib import Path


def leer_csv_login(ruta_csv: str = "data/login.csv"):
    """
    Devuelve una lista de tuplas: (usuario, password, espera_ok)
    espera_ok: True/False
    """
    ruta = Path(ruta_csv)

    filas = []
    with ruta.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            usuario = row["usuario"].strip()
            password = row["password"].strip()



            # convierte 1/0 a True/False para que quede mas claro en el test
            espera_ok_str = row["espera_ok"].strip()

            #el strip limpia el texto sacando espacios y saltos de lineas como
            #hace trim en js(anotacion personal)
            espera_ok = True if espera_ok_str == "1" else False

            filas.append((usuario, password, espera_ok))

    return filas


def leer_json_productos(ruta_json: str = "data/productos.json"):
    """
    Devuelve una lista de tuplas: (nombre, add_button_id)
    """
    with open(ruta_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    productos = []
    for p in data["productos"]:
        nombre = p["nombre"].strip()
        add_id = p["add_button_id"].strip()
        productos.append((nombre, add_id))

    return productos