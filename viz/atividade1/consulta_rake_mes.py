import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo
caminho_arquivo = 'C:/Users/lsoliveira/Documents/H2Club_teste/atividade1/resultado_query/consulta_rake_mes.csv'

# Lendo o arquivo CSV
df = pd.read_csv(caminho_arquivo)

# Convertendo a coluna 'Data' para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m')

# Ordenando o dataframe pela coluna 'Data'
df = df.sort_values(by='Data')

# Função para anotar os valores nos pontos máximos e mínimos
def annotate_max_min_corrected(x, y, ax):
    max_val = y.max()
    min_val = y.min()
    max_index = y.idxmax()
    min_index = y.idxmin()
    
    ax.annotate(f"{max_val:.2f}", (x[max_index], max_val), textcoords="offset points", xytext=(0,5), ha='center')
    ax.annotate(f"{min_val:.2f}", (x[min_index], min_val), textcoords="offset points", xytext=(0,5), ha='center')

# Função para adicionar linhas de grade personalizadas
def updated_custom_grid(ax):
    # Linhas de grade horizontais
    for y_value in [20000, 40000, 60000, 80000]:
        ax.axhline(y=y_value, color='lightgray', linestyle='-', linewidth=0.5)
    
    # Linhas de grade verticais
    for x_value in ['2021-01', '2022-01', '2023-01']:
        ax.axvline(x=pd.Timestamp(x_value), color='lightgray', linestyle='-', linewidth=0.5)

# Configurando o gráfico
plt.figure(figsize=(12, 6))
ax = plt.gca()
ax.plot(df['Data'], df['Total_Rake'], marker='o', linestyle='-')

# Anotar valores nos pontos máximos e mínimos
annotate_max_min_corrected(df['Data'], df['Total_Rake'], ax)

# Configurações visuais
plt.title('Total Rake ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Total Rake')
ax.get_yaxis().set_ticks([80000,60000,40000,20000])  # Remove os ticks do eixo Y
plt.tight_layout()
plt.xticks(rotation=45)

# Adicionando linhas de grade personalizadas
updated_custom_grid(ax)

# Mostra o gráfico
plt.show()
