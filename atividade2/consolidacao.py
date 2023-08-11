import pandas as pd

def consolidate(df):
    # Processar dados
    df['datahora_acesso'] = pd.to_datetime(df['datahora_acesso'])
    df['mes'] = df['datahora_acesso'].dt.month

    # Criar colunas intermediárias para cada condição usando operações vetorizadas
    df['rake_cash_game'] = df['rake'].where(df['modalidade'] == 'Cash Game', 0)
    df['rake_torneio'] = df['rake'].where(df['modalidade'] == 'Torneio', 0)
    df['jogador_cash_game'] = (df['modalidade'] == 'Cash Game').astype(int)
    df['jogador_torneio'] = (df['modalidade'] == 'Torneio').astype(int)

    # Agregando os dados
    grouped = df.groupby('mes').agg(
        rake=('rake', 'sum'),
        jogadores=('clientes_id', 'nunique'),
        rake_cash_game=('rake_cash_game', 'sum'),
        rake_torneio=('rake_torneio', 'sum'),
        jogadores_cash_game=('jogador_cash_game', 'sum'),
        jogadores_torneio=('jogador_torneio', 'sum')
    ).reset_index()

    return(grouped)