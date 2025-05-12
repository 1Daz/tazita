import os
import json

def read(path_file):
    if not os.path.exists(path_file):
        print(f"Error: The file '{path_file}' does not exist.")
        return None

    try:
        with open(path_file, 'r', encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: The file '{path_file}' contains invalid JSON:\n{e}")
        return None
    except Exception as e:
        print(f"Unexpected error reading the file '{path_file}':\n{e}")
        return None

    return data

def main():
    file_json = "tasks.json"
    path_file = os.path.join('data', file_json)
    processed_data = read(path_file)

    if processed_data:
        print(processed_data)

        files_dir = "files"
        if not os.path.exists(files_dir):
            os.makedirs(files_dir)
            print(f"Folder '{files_dir}' created.")

        output_file_path = os.path.join(files_dir, "output.json")

        try:
            with open(output_file_path, "w", encoding="utf-8") as outfile:
                json.dump(processed_data, outfile, indent=4)
            print(f"Data saved to '{output_file_path}'")
        except Exception as e:
            print(f"Error writing to file '{output_file_path}':\n{e}")

