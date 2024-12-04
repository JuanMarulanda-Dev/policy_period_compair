from src.services.DBService import DBService
from src.services.ImportService import ImportService

def import_data_from_PC():
    print("Importando data de PC")
    #  Crear una conexión a la base de datos
    db_name = "CS.db"
    db_service = DBService(db_name)

    conn = db_service.connect()
    query = '''
    CREATE TABLE IF NOT EXISTS PoliciesPC (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        master TEXT NOT NULL,
        risk TEXT NOT NULL,
        numberOfRenewals INTEGER NOT NULL,
        beneficiaries INTEGER NOT NULL,
        FOREIGN KEY (master) REFERENCES PoliciesCS(npoliza)
    )
    '''
    db_service.create_table(conn, query)
    import_service = ImportService(conn)

    csv_file_path = "C:\\Users\\juan.marulanda\\Desktop\\policy-period-compair\\db2_data\\export_pc.cvs"
    import_service.import_from_cvs(csv_file_path)

    conn.close()

    print("Datos importados con éxito a la tabla PoliciesPC.")

if __name__ == '__main__':
    #Importando data de CS a SQLite
    import_data_from_PC()