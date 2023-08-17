import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo
caminho_arquivo = 'C:/Users/lsoliveira/Documents/H2Club_teste/atividade1/resultado_query/consulta_sexo_proporcao.csv'

# Lendo o arquivo CSV
df_sexo = pd.read_csv(caminho_arquivo)

# Substituindo "NaN" por "Null"
df_sexo['Sexo'].fillna('Null', inplace=True)

# Removendo a linha com o valor "Total"
df_sexo = df_sexo[df_sexo['Sexo'] != 'Total']

# Criando o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(df_sexo['Percentual'], labels=df_sexo['Sexo'], autopct='%1.1f%%', startangle=140, colors=['#00BFFF', '#DCDCDC', '#EE82EE', '#FFCC99'])
plt.title('Proporção de Ganhadores por Sexo')
plt.tight_layout()

# Mostra o gráfico
plt.show()
