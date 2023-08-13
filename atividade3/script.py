from processar_dados import processar
from salvar_dados import salvar

def main():
    try:
        # Processar os dados
        dados_filtrados = processar()

        # Salvar os dados no SQLite
        salvar(dados_filtrados)

        print("Execução do script foi bem sucedida!")

    except Exception as e:
        print(f"Ocorreu um erro durante a execução do script: {e}")

# Executa a função main quando o script é executado
if __name__ == "__main__":
    main()
