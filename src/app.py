# Importamos herramientas que necesitamos: os para trabajar con el sistema operativo,
# time para manejar tiempos, pandas para trabajar con tablas de datos, y algunas cosas
# de sqlalchemy para conectarnos y trabajar con bases de datos.
import os
import time
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
# Cargamos las variables de entorno desde un archivo .env.
# Las variables de entorno son como secretos o configuraciones que guardamos aparte.
load_dotenv()
# Creamos una cadena de conexión para la base de datos usando las variables de entorno.
# Es como una dirección para decirle a Python cómo encontrar y conectarse a la base de datos.
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
# Creamos un 'motor' para conectarnos a la base de datos. Es como un carro que nos lleva a la base de datos.
engine = create_engine(connection_string, echo=True)  # echo=True mostrará las consultas SQL ejecutadas
# Intentamos hacer varias cosas con la base de datos, pero si algo sale mal, lo diremos.
try:
    # Conectamos a la base de datos usando nuestro 'motor'.
    with engine.connect() as connection:
        print("Base de datos conectada.")
        # Intentamos crear tablas en la base de datos usando un archivo .sql.
        try:
            # Decimos dónde está el archivo que tiene las instrucciones para crear las tablas.
            filepath = '/workspaces/SQL/src/sql/create.sql'
            # Abrimos el archivo y leemos lo que dice.
            with open(filepath, 'r') as f:
                sql_script = f.read()
            # Ejecutamos cada instrucción en el archivo, una por una.
            for statement in sql_script.split(';'):
                if statement.strip():  # Nos aseguramos de que la instrucción no esté vacía.
                    connection.execute(text(statement))
            print("Tablas creadas exitosamente.")
        # Si algo sale mal al crear las tablas, lo decimos.
        except Exception as e:
            print(f"Error al crear las tablas: {str(e)}")
        # Esperamos un poquito para asegurarnos de que las tablas estén listas antes de seguir.
        time.sleep(1)
        # Ahora intentamos poner datos en las tablas.
        try:
            # Decimos dónde está el archivo que tiene las instrucciones para poner los datos.
            insert_sql_path = '/workspaces/SQL/src/sql/insert.sql'
            # Abrimos ese archivo y leemos lo que dice.
            with open(insert_sql_path, 'r') as f:
                insert_sql_script = f.read()
            # Ejecutamos cada instrucción en el archivo, una por una.
            for statement in insert_sql_script.split(';'):
                if statement.strip():  # Nos aseguramos de que la instrucción no esté vacía.
                    connection.execute(text(statement))
            print("Datos insertados con éxito.")
        # Si algo sale mal al poner los datos, lo decimos.
        except Exception as e:
            print(f"Error al insertar datos: {str(e)}")
        # Esperamos un poquito para asegurarnos de que los datos estén listos antes de seguir.
        time.sleep(1)
        # Ahora intentamos borrar las tablas.
        try:
            # Decimos dónde está el archivo que tiene las instrucciones para borrar las tablas.
            drop_sql_path = '/workspaces/SQL/src/sql/drop.sql'
            # Abrimos ese archivo y leemos lo que dice.
            with open(drop_sql_path, 'r') as file:
                drop_sql_script = file.read()
            # Ejecutamos cada instrucción en el archivo, una por una.
            for statement in drop_sql_script.split(';'):
                if statement.strip():  # Nos aseguramos de que la instrucción no esté vacía.
                    connection.execute(text(statement))
            print("Tablas eliminadas con éxito.")
        # Si algo sale mal al borrar las tablas, lo decimos.
        except Exception as e:
            print(f"Error al eliminar tablas: {str(e)}")
        # Ahora intentamos ver los datos en una de las tablas.
        try:
            # Escribimos la instrucción para pedir todos los datos de la tabla 'publishers'.
            query = "SELECT * FROM publishers;"
            # Usamos pandas, que es bueno para trabajar con tablas, para obtener los datos y mostrarlos.
            df_publishers = pd.read_sql(query, connection)
            # Mostramos los datos en la pantalla.
            print("Tabla PUBLISHERS:")
            df_publishers = pd.DataFrame(df_publishers)
            print(df_publishers)
        # Si algo sale mal al intentar ver los datos, lo decimos.
        except Exception as e:
            print(f"Error al leer los datos: {str(e)}")
# Si algo sale mal al intentar conectarnos a la base de datos en general, lo decimos.
except Exception as e:
    print(f"No se puede conectar a la base de datos: {str(e)}")