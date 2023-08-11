from conexao import conexao
from read_data import read_data
from consolidacao import consolidate
from salvamento import salvar

try:
    engine = conexao()
    df = read_data(engine)
    grouped = consolidate(df)
    salvar(grouped)
    print("Execução do script foi bem sucedida!")

except Exception as e:
    print(f"Ocorreu um erro durante a execução do script: {e}")
