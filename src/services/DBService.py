import sqlite3

class DBService:
    def __init__(self, db_name):
        """Inicializa el servicio con el nombre de la base de datos."""
        self.db_name = db_name

    def connect(self):
        """Crea una conexión a la base de datos."""
        try:
            conn = sqlite3.connect(self.db_name)
            print(f"Conectado a la base de datos {self.db_name}")
            return conn
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def create_table(self, conn, create_table_sql):
        """Crea una tabla en la base de datos dada una conexión y una sentencia SQL."""
        try:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
            conn.commit()
            print("Tabla creada exitosamente")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def execute_sql(self, conn, sql):
        """Ejecuta una sentencia SQL en una conexión dada."""
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            print("Sentencia SQL ejecutada exitosamente")
        except sqlite3.Error as e:
            print(f"Error al ejecutar la sentencia SQL: {e}")
