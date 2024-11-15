import json
import sqlite3

class ImportService:
    def __init__(self, connection):
        """Inicializa el servicio con una conexión a la base de datos."""
        self.connection = connection

    def import_from_json(self, json_file_path):
        """Importa datos desde un archivo JSON a una tabla especificada en la base de datos."""
        try:
            # Leer el archivo JSON
            with open(json_file_path, 'r') as file:
                data = json.load(file)

            items = data.get('items', [])

            # Preparar la sentencia SQL para insertar datos
            insert_sql = f"INSERT INTO PolicesCS (npoliza, cantidad_beneficiarios) VALUES (?, ?)"

            # Insertar cada item en la tabla
            cursor = self.connection.cursor()
            for item in items:
                cursor.execute(insert_sql, (item['npoliza'], item['cantidad_beneficiarios']))

            # Confirmar los cambios
            self.connection.commit()
            print(f"Datos importados exitosamente a la tabla PolicesCS")
        except (sqlite3.Error, json.JSONDecodeError) as e:
            print(f"Error al importar datos: {e}")


    def import_from_plain_text(self, text_file_path):
        print("Hola mundo")