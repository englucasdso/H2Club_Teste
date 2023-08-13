from processar_dados import processar
from sqlalchemy import create_engine
import pandas as pd

def salvar(filtered_data):
    # Convertendo os dados para um DataFrame
    df = pd.DataFrame(filtered_data)

    # Definindo o caminho do banco de dados SQLite
    database_path = "partidas_brasileirao_serie_a_2023.sqlite"

    # Criar engine para SQLite
    engine_sqlite = create_engine(f"sqlite:///{database_path}")

    # Salvar dados consolidados no SQLite
    table_name = 'partidas_brasileirao_serie_a_2023'
    if not engine_sqlite.has_table(table_name):
        df.to_sql(table_name, engine_sqlite, index=False)
    else:
        df.to_sql(table_name, engine_sqlite, if_exists='append', index=False)

if __name__ == "__main__":
    dados_filtrados = processar()
    salvar(dados_filtrados)
    print("Dados salvos com sucesso!")
