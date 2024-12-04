import json
import sqlite3
import csv

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
            insert_sql = '''INSERT INTO PoliciesCS (master, numberOfRenewals) 
                            VALUES (?, ?)'''

            # Insertar cada item en la tabla
            cursor = self.connection.cursor()
            for item in items:
                cursor.execute(insert_sql, (item['npoliza'], item['cantidad_beneficiarios']))

            # Confirmar los cambios
            self.connection.commit()
            print("Datos importados exitosamente a la tabla PolicesCS")
        except (sqlite3.Error, json.JSONDecodeError) as e:
            print(f'Error al importar datos: {e}')


    def import_from_cvs(self, cvs_file_path):
        try:

            cursor = self.connection.cursor()

            # Preparar la sentencia SQL para insertar datos
            insert_sql = '''
                    INSERT INTO PoliciesPC (master, risk, numberOfRenewals, beneficiaries)
                    VALUES (?, ?, ?, ?)
                    '''

            # Leer el archivo CSV e insertar los datos en la tabla PoliciesPC
            with open(cvs_file_path, mode='r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=';')

                for row in csv_reader:
                    master, risk, number_of_renewals, beneficiaries = row
                    cursor.execute(insert_sql, (master, risk, int(number_of_renewals), int(beneficiaries)))

            # Confirmar los cambios
            self.connection.commit()
            print("Datos importados exitosamente a la tabla PolicesPC")
        except (sqlite3.Error, json.JSONDecodeError) as e:
            print(f'Error al importar datos: {e}')