from src.services.DBService import DBService

def main():
    db_service = DBService('CS.db')
    conn = db_service.connect()
    cursor = conn.cursor()

    # Consultar registros
    cursor.execute('SELECT * FROM PolicesCS')
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila)

    conn.close()



if __name__ == '__main__':
    main()
