import mysql.connector
from sqlalchemy import create_engine

def conexao():
    # Dados da conexão
    host = '40b8f30251.nxcli.io'
    db = 'a4f2b49a_sample_database'
    user = 'a4f2b49a_padawan'
    passwd = 'KaratFlanksUgliedSpinal'
    port = 3306 

    # Criar conexão
    connection_string = f"mysql+mysqlconnector://{user}:{passwd}@{host}:{port}/{db}"
    engine = create_engine(connection_string)
    return engine
