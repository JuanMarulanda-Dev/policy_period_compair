import json

def fix_json_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read()

    # Reemplazar los }{ con },{ para agregar comas donde faltan
    corrected_content = content.replace('}{', '},{')

    # Intentar cargar el JSON para verificar si es válido
    try:
        json_data = json.loads(corrected_content)
        # Guardar el JSON corregido en un nuevo archivo
        with open(output_file_path, 'w') as output_file:
            json.dump(json_data, output_file, indent=4)
        print("JSON corregido y guardado exitosamente.")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el JSON: {e}")

# Ejemplo de uso
input_file_path = "C:\\Users\\juan.marulanda\\Desktop\\export.json"
output_file_path = "C:\\Users\\juan.marulanda\\Desktop\\export_fix.json"
fix_json_file(input_file_path, output_file_path)


if __name__ == '__main__':
    fix_json_file("C:\\Users\\juan.marulanda\\Desktop\\export.json", "C:\\Users\\juan.marulanda\\Desktop\\export_fix.json")