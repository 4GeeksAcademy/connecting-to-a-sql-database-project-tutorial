# Conectarse a una base de datos SQL usando Python

## Parte 1: Crea una base de datos usando PostgreSQL

Asegúrate de tener instalado el cliente de Postgres para la terminal llamado `PSQL`. Puedes verificar si lo tienes corriendo el siguiente comando:

```bash
$ psql --version
```

> NOTA: Si da un error, intenta [seguir las instrucciones en este artículo](https://www.timescale.com/blog/how-to-install-psql-on-mac-ubuntu-debian-windows/) para instalar `psql` en tu computadora.

A continuación, revisa el contenido del archivo `./.env` y sigue los pasos que se describen a continuación:

1. Crea una nueva base de datos dentro del motor de Postgres personalizando y ejecutando el siguiente comando: `$ createdb -h localhost -U <username> <db_name>`
2. Conéctate al motor de Postgres para utilizar tu base de datos, manipular tablas y datos:  `$ psql -h localhost -U <username> <db_name>`

> NOTA: Recuerda revisar la información del fichero `./.env` para obtener el `username` y el `db_name`.

¡Cuanto estés dentro de PSQL podrás crear tablas, hacer consultas, insertar, actualizar o eliminar datos y mucho más!

## Parte 2: Comprende la estructura de la plantilla de tu proyecto

Una vez hayas completado los pasos anteriores, habrás creado tu base de datos SQL, pero aún no hay tablas. A continuación, debes conectarte a tu base de datos vacía y crearás algunas tablas usando Python mediante scripts SQL que encontrarás en la carpeta `./src/sql/`:

- `./src/sql/create.sql` con todas las tablas que necesitas crear. Manos a la obra en la creación de esas tablas.
- `./src/sql/insert.sql` con todos los registros que se insertarán en cada tabla.
- `./src/sql/drop.sql` contiene el código SQL para borrar las tablas, muy útil para limpiar tu base de datos.

Otras cosas importantes a mencionar sobre la estructura:

- Los proyectos profesionales suelen tener una carpeta `./src` que contiene todos los **archivos de código** (los archivos que implementará el desarrollador).
- `./assets` es irrelevante para ti, contiene todas las imágenes que necesitábamos para este tutorial.
- La raíz (*root*) de cualquier proyecto profesional suele contener todos los archivos de configuración como `.gitignore`, `requirements.txt`, etc. Aprenderás más sobre estos archivos durante el resto del proyecto.

## Parte 3: Instala dependencias

Hay un archivo en este proyecto llamado `./requirements.txt` que contiene la lista de bibliotecas de Python que usaremos en este proyecto como Pandas, psycopg2, SQLAlchemy, etc. Ejecuta el comando `pip install -r requirements.txt` para instalar todas las bibliotecas a la vez usando el asistente PIP (*Package Installer of Python*, Instalador de Paquetes de Python).

> NOTA: Asegúrate de que el comando no genere ningún error en el terminal.

## Parte 4: Incluye las credenciales de tu base de datos

Crea tu archivo `./.env`. Es una buena práctica que cada aplicación de Python tenga un archivo `.env`. El nombre del archivo comienza con un punto `.` porque es un archivo de configuración que será ignorado por tu repositorio Git. Debe ignorarse porque agregaremos la contraseña de nuestra base de datos dentro de ese archivo.

Escribe las credenciales de tu base de datos dentro del archivo `.env`. Debería quedar algo así (los valores que se incluyen son de ejemplo):

```text
DB_USER = 'hkietatgd83b4x0l'
DB_PASSWORD = 'p0s2wasdado1cr02d12'
DB_PORT = 3306
DB_HOST = 'f565gmi022AD.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
DB_NAME = 'y9uflxvx2hsf11g3f'
```

> NOTA: Asegúrate de reemplazar estos valores con tus credenciales de base de datos reales.

## Parte 5: Empieza a programar

Todo tu código de Python siempre debe estar dentro de la carpeta `src`, esta también es otra buena práctica.

1. La función `connect` contiene el código necesario para conectarse a tu base de datos de Python. Si observas con atención verás cómo carga todas las variables de entorno en una variable llamada `connection_string` y luego llama a las funciones `create_engine` y `connect`.

```py
def connect():
    global engine # Esto nos permite usar una variable global llamada "engine"
    # Un "connection string" es básicamente una cadena que contiene todas las credenciales de la base de datos juntas
    connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
    print("Starting the connection...")
    engine = create_engine(connection_string)
    engine.connect()
    return engine
```

## 📝 Instrucciones

1. Vamos a crear un archivo dentro de la carpeta `src` llamado `./src/app.py`.

> NOTA: Este archivo contendrá la mayor parte del código de tu aplicación, así como la conexión a la base de datos y las consultas a la base de datos.

2. Crea una base de datos PostgreSQL tal y como se indica en la parte 1.

3. En tu `app.py`, programa la conexión con tu base de datos.

> NOTA: Puedes tratar de reutilizar la función de Python `connect` anteriormente facilitada.

4. Crea las tablas indicadas en `./src/sql/create.sql`.

5. Inserta los datos indicados de `./src/sql/insert.sql` en las tablas creadas en el punto anterior.

6. Usa Pandas para imprimir una de las tablas como DataFrame usando la función `read_sql` de esta librería.

## Tips adicionales

- Inicia sesión en tu base de datos usando: `psql -h localhost -u postgres`
- Conéctate a una base de datos remota usando: `psql -h <REMOTE_HOST> -p <REMOTE_PORT> -U <DB_USER> <DB_NAME>`
- Elimina una base de datos: `$ dropdb -h localhost -U <username> <db_name>`
- Crea una BD en la nube de render.com y conéctate [siguiendo estos comandos](https://render.com/docs/databases#connecting-from-outside-render).

