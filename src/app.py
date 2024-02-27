import os
import time
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Crear la cadena de conexión a la base de datos utilizando las variables de entorno
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string, echo=True)  # echo=True mostrará las consultas SQL ejecutadas

try:
    # Conectar a la base de datos
    with engine.connect() as connection:
        print("Base de datos conectada.")

        # 2) Crear Tablas
        # Intentar ejecutar el script de creación de tablas desde un archivo .sql
        try:
            # Ruta al archivo que contiene las sentencias SQL para crear las tablas
            filepath = '/workspaces/zalo-sql/src/sql/create.sql'
            
            # Abrir y leer el archivo SQL
            with open(filepath, 'r') as f:
                sql_script = f.read()
            
            # Ejecutar cada sentencia SQL por separado
            for statement in sql_script.split(';'):
                if statement.strip():  # Verificar que la sentencia no esté vacía
                    connection.execute(text(statement))
            
            print("Tablas creadas exitosamente.")
        
        # Manejar cualquier error durante la creación de las tablas
        except Exception as e:
            print(f"Error al crear las tablas: {str(e)}")
        
        # Pausar para asegurarnos de que todas las tablas han sido creadas antes de insertar datos
        time.sleep(1)
        
        # 3) Insertar Datos
        # Intentar ejecutar el script de inserción de datos desde un archivo .sql
        try:
            # Ruta al archivo que contiene las sentencias SQL para insertar los datos
            insert_sql_path = '/workspaces/zalo-sql/src/sql/insert.sql'
            
            # Abrir y leer el archivo SQL
            with open(insert_sql_path, 'r') as f:
                insert_sql_script = f.read()
            
            # Ejecutar cada sentencia SQL por separado
            for statement in insert_sql_script.split(';'):
                if statement.strip():  # Verificar que la sentencia no esté vacía
                    connection.execute(text(statement))
            
            print("Datos insertados con éxito.")
        
        # Manejar cualquier error durante la inserción de datos
        except Exception as e:
            print(f"Error al insertar datos: {str(e)}")

        # Pausar para asegurarnos de que todos los datos han sido insertados antes de realizar consultas
        time.sleep(1)

        # 4) Recuperar y Mostrar Datos
        # Intentar recuperar datos de la tabla 'publishers' y mostrarlos utilizando pandas
        try:
            # Sentencia SQL para recuperar todos los datos de la tabla 'publishers'
            query = "SELECT * FROM publishers;"
            
            # Utilizar pandas para realizar la consulta y mostrar los datos en un DataFrame
            df_publishers = pd.read_sql(query, connection)
            
            # Mostrar el DataFrame en consola
            print("Tabla PUBLISHERS:")
            print(df_publishers)
        
        # Manejar cualquier error durante la recuperación y visualización de datos
        except Exception as e:
            print(f"Error al leer los datos: {str(e)}")

# Manejar cualquier error durante la conexión a la base de datos
except Exception as e:
    print(f"No se puede conectar a la base de datos: {str(e)}")