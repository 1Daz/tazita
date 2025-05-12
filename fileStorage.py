import os
import json

def leer_y_procesar_json(path_file):
    if not os.path.exists(path_file):
        print(f"Error: El archivo '{path_file}' no existe.")
        return None
    try:
        with open(path_file, 'r', encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: El archivo '{path_file}' no contiene JSON válido:\n{e}")
        return None
    except Exception as e:
        print(f"Error inesperado al leer el archivo '{path_file}':\n{e}")
        return None

    return data

def main():
    file_json = "tasks.json"
    path_file = os.path.join('data', file_json)
    processed_data = leer_y_procesar_json(path_file)

    if processed_data:
        print(processed_data)
        files_dir = "files"
        if not os.path.exists(files_dir):
            os.makedirs(files_dir)
            print(f"Carpeta '{files_dir}' creada.")

        output_file_path = os.path.join(files_dir, "output.json")
        try:
            with open(output_file_path, "w", encoding="utf-8") as outfile:
                json.dump(processed_data, outfile, indent=4)  # indent para formato legible
            print(f"Datos guardados en '{output_file_path}'")
        except Exception as e:
            print(f"Error al escribir en el archivo '{output_file_path}':\n{e}")

if __name__ == "__main__":
    main()
