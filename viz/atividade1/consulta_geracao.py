import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo
caminho_arquivo = 'C:/Users/lsoliveira/Documents/H2Club_teste/atividade1/resultado_query/consulta_geracao.csv'

# Lendo o arquivo CSV
df_geracao = pd.read_csv(caminho_arquivo)

# Função para anotar os valores na frente de cada barra com uma casa decimal
def annotate_bars_decimal(values, ax):
    for i, v in enumerate(values):
        ax.text(v + 10000, i, f"{v:.1f}", va='center', color='black', fontweight='normal')

# Função para formatar os rótulos do eixo Y com os anos das gerações
def format_ylabels(geracoes, periodos):
    return [f"{ger} ({per})" for ger, per in zip(geracoes, periodos)]

# Configurando o gráfico de barras horizontais
plt.figure(figsize=(12, 6))
ax = plt.gca()
bars = ax.barh(df_geracao['Geracao'], df_geracao['Total_Rake'], color='skyblue')

# Anotando os valores nas barras com uma casa decimal
annotate_bars_decimal(df_geracao['Total_Rake'], ax)

# Configurações visuais
plt.xlabel('Total Rake')
plt.ylabel('Geração')
plt.title('Total Rake por Geração')
plt.xticks([200000, 400000, 600000])
ax.set_yticklabels(format_ylabels(df_geracao['Geracao'], df_geracao['Periodo_nascimento']), color='gray', fontsize=10)
plt.grid(False)

plt.tight_layout()

# Mostra o gráfico
plt.show()
