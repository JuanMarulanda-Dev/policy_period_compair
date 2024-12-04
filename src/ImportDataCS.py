from src.services.DBService import DBService
from src.services.ImportService import ImportService

def main():
    print("Importando data de CS")
    # Crear una conexión a la base de datos
    db_name = "CS.db"
    db_service = DBService(db_name)

    conn = db_service.connect()
    query = """CREATE TABLE IF NOT EXISTS PoliciesCS (
            master TEXT PRIMARY KEY,
            numberOfRenewals INTEGER NOT NULL
        );"""
    db_service.create_table(conn, query)

    # Crear una instancia del servicio de importación
    import_service = ImportService(conn)

    # Importar datos desde un archivo JSON
    json_file_path = "C:\\Users\\juan.marulanda\\Desktop\\policy-period-compair\\db1_data\\export_fix.json"
    import_service.import_from_json(json_file_path)

    conn.close()

if __name__ == '__main__':
    #Importando data de CS a SQLite
    main()

