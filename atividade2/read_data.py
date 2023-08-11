import pandas as pd

def read_data(engine):
    # Ler dados
    df = pd.read_sql('SELECT * FROM raw_data', engine)
    return df
