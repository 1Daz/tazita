import os
import json

def leerJson(path_file):

    if os.path.exists(path_file):
        try:
            with open(path_file, 'r', encoding="utf-8") as f:
                data = json.load(f)
            print("\n----------- A -----------")
            def simplify(datos):
                if isinstance(datos, dict):
                    for clave, valor in datos.items():
                        if clave == "id":
                            print(f"ID: {valor}")
                        elif clave == "descripcion":
                            print(f"Descripción: {valor}")
                        else:
                            print(f"{clave.capitalize()}: {valor}") 
                    print("\n")
                elif isinstance(datos, list):
                    for item in datos:
                        simplify(item)
                else:
                    print(datos)

            simplify(data)

        except json.JSONDecodeError:
            print(f"Error: El archivo '{path_file}' no contiene JSON válido.")
    else:
        print(f"The file '{path_file}' doesn't exist!")

    if not os.path.exists("files"):
        os.makedirs("files")
        print("Folder <files> has just been created!")
