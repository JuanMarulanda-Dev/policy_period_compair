from src.services.DBService import DBService

def getPolicesCS():
    db_service = DBService('CS.db')
    conn = db_service.connect()
    cursor = conn.cursor()

    # Consultar registros
    cursor.execute('SELECT * FROM PolicesCS')
    policies = cursor.fetchall()

    for policy in policies:
        print(f'"{policy[0]}",')

    conn.close()

def getPolicesPC():
    db_service = DBService('CS.db')
    conn = db_service.connect()
    cursor = conn.cursor()

    # Consultar registros
    cursor.execute('SELECT * FROM PoliciesPC')
    policies = cursor.fetchall()

    for policy in policies:
        print(policy)

    conn.close()

def getDifferencesBetweenCSAndPC():
    # Conectar a la base de datos SQLite
    db_service = DBService('CS.db')
    conn = db_service.connect()
    cursor = conn.cursor()

    # Definir el query
    query = '''
    SELECT 
        PoliciesCS.master,
        PoliciesCS.numberOfRenewals,
        PoliciesPC.numberOfRenewals
    FROM 
        PoliciesCS
    JOIN 
        PoliciesPC
    ON 
        PoliciesCS.master = PoliciesPC.master
    WHERE 
        PoliciesCS.numberOfRenewals != PoliciesPC.numberOfRenewals;
    '''

    # Ejecutar el query
    cursor.execute(query)
    resultados = cursor.fetchall()

    # Cerrar la conexión
    conn.close()

    # Imprimir los resultados
    for fila in resultados:
        print(f"master: {fila[0]}, numberOfRenewalsCS: {fila[1]}, numberOfRenewalsPC: {fila[2]}")

if __name__ == '__main__':
    getDifferencesBetweenCSAndPC()
