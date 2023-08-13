# Teste para Engenheiro de Dados - H2 Club

Este é um teste da H2 Club com o intuito de avaliar as minhas seguintes habilidades: conhecimento em SQL, Python, manipulação de dados, utilização de API's e documentação de projetos.

## Índice

- [Atividade 1 - Consultas SQL](#atividade-1---consultas-sql)
- [Atividade 2 - Manipulação de Dados em Python](#atividade-2---manipulação-de-dados-em-python)
- [Atividade 3 - Acessando APIs com Python](#atividade-3---acessando-apis-com-python)
- [Considerações Finais](#considerações-finais)

## Atividade 1 - Consultas SQL

Nesta atividade, o foco foi explorar dois arquivos csv, utilizando consultas SQL para extrair informações específicas. As questões abordaram diferentes aspectos, desde consultas básicas até junções um pouco mais complexas e funções agregadas.

- **Pergunta 1**: Quanto de rake foi gerado por cada Geração* de jogadores? [Link para o arquivo](./atividade1/query/consulta_geracao.sql)
- **Pergunta 2**: Qual foi o rake gerado por mês? [Link para o arquivo](./atividade1/query/consulta_rake_mes.sql)
- **Pergunta 3**: Qual sexo tem uma maior proporção de ganhadores? [Link para o arquivo](./atividade1/query/consulta_sexo_proporcao.sql)

- **Resultado Pergunta 1**: Geração y obteve maior rake e veteranos foi retirado da análise por não retornar dados. [Link para o arquivo](./atividade1/resultado_query/consulta_geracao.csv)
- **Resultado Pergunta 2**: O periodo com maior rake foi o ano de 2022, mantendo todos os rakes acima de 40.000.00. [Link para o arquivo](./atividade1/resultado_query/consulta_rake_mes.csv)
- **Resultado Pergunta 3**: 84% do publico é do sexo masculino, 6% feminino e o restante não foi identificado. [Link para o arquivo](./atividade1/resultado_query/consulta_sexo_proporcao.csv)

## Atividade 2 - Manipulação de Dados em Python

A segunda atividade envolveu a manipulação e transformação de dados utilizando Python. O desafio era extrair dados de um banco de dados MySQL, processá-los e, posteriormente, armazená-los em um MySQL localmente (utilizei SQLite). Durante este processo, foram aplicadas diversas técnicas de limpeza e transformação de dados com a biblioteca Pandas, garantindo que os dados estivessem no formato correto e prontos para análises futuras. 

- **Script de Transformação**: [Link para o script](./atividade2/script.py)

## Atividade 3 - Acessando APIs com Python

Neste último desafio, a tarefa era acessar uma API externa para obter dados de partidas de esportes. A complexidade residia em filtrar e formatar corretamente os dados recebidos, focando especificamente em partidas do campeonato brasileiro de 2023. Após a obtenção e processamento dos dados, a etapa final consistia em armazená-los localmente, garantindo que todas as informações estivessem corretamente estruturadas e prontas para consulta.

- **Script da API**: [Link para o script](./atividade3/script.py)

## Considerações Finais

Durante a realização deste teste, enfrentei diversos desafios que enriqueceram minha experiência e me proporcionaram um aprendizado valioso. A integração com a API, em particular, apresentou algumas nuances, como a necessidade de ajustar os parâmetros e a URL para obter os dados corretos. Além disso, a manipulação e processamento de dados em Python exigiu uma abordagem cuidadosa, especialmente ao lidar com diferentes estruturas de dados e garantir que as informações fossem filtradas e armazenadas corretamente.

Optei por utilizar SQLite por não ter permissão para baixar o MySQL, pois não tenho maquina pessoal e utilizo da empresa atual. Utilizei um design lógico no código para garantir a modulardade e reutilização, dividindo as tarefas em funções distintas e arquivos separados.

Gostaria de agradecer pela oportunidade de realizar este teste, pois ele me permitiu aplicar e expandir meus conhecimentos em áreas cruciais da Engenharia de Dados. Estou ansioso pelo feedback e aberto a discussões sobre as soluções propostas.

Obrigado!