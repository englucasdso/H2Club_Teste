import pandas as pd
from acessar_api import acessar

def processar():
    data_json = acessar()  # chama a função para obter os dados
    
    # Convertendo o JSON para um DataFrame
    df = pd.DataFrame(data_json)

    # Filtrar e formatar os dados
    filtered_data = []

    for _, row in df.iterrows():
        if row['sport_key'] == "soccer_brazil_campeonato" and "2023" in row['commence_time']:
            home_score = None
            away_score = None
            
            if row['scores'] is not None:
                for score in row['scores']:
                    if score['name'] == row['home_team']:
                        home_score = score['score']
                    elif score['name'] == row['away_team']:
                        away_score = score['score']
                        
            filtered_data.append({
                "datahora_partida": row['commence_time'],
                "data_partida": row['commence_time'].split('T')[0],  # Extrai apenas a data
                "time_casa": row['home_team'],
                "time_fora": row['away_team'],
                "gols_time_casa": home_score,
                "gols_time_fora": away_score
            })
    
    return filtered_data  # retorna os dados filtrados

