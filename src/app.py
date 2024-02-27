import os
from sqlalchemy import create_engine, String, Column, Table, Integer, insert
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.orm import Session

load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
engine.connect()



# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
from sqlalchemy import MetaData
meta = MetaData()
informacion = Table(
   'informacion', meta, 
   Column('DNI', Integer, primary_key = True), 
   Column('Nombre', String), 
   Column('Apellido', String), 
)

meta.create_all(engine)

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

conn = engine.connect() 
  
filas = [ 
    (456, 'Juan', 'Gutierrez'), 
    (247, 'Pedro', 'Hernandez'), 
    (5679, 'Lola', 'Frias') 
]
  
stmt = insert(informacion).values( 
    [{'DNI': dni, 'Nombre': nombre, 'Apellido': apellidos} for dni, nombre, apellidos in filas]) 
# conn.execute(stmt) 
with Session(engine) as session:
    result = session.execute(stmt)
    session.commit()


# 4) Use pandas to print one of the tables as dataframes using read_sql function

import pandas as pd

result_dataFrame = pd.read_sql("Select * from informacion;", engine)
print(result_dataFrame)