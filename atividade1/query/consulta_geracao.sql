#consulta_feita_no_google_bigquery

#Quanto de rake foi gerado por cada geracao de jogadores?

SELECT
    CASE
        WHEN EXTRACT(YEAR FROM data_nascimento) BETWEEN 1925 AND 1940 THEN 'Veteranos'
        WHEN EXTRACT(YEAR FROM data_nascimento) BETWEEN 1941 AND 1959 THEN 'Baby Boomers'
        WHEN EXTRACT(YEAR FROM data_nascimento) BETWEEN 1960 AND 1979 THEN 'Geração X'
        WHEN EXTRACT(YEAR FROM data_nascimento) BETWEEN 1980 AND 1995 THEN 'Geração Y'
        WHEN EXTRACT(YEAR FROM data_nascimento) BETWEEN 1996 AND 2010 THEN 'Geração Z'
        ELSE 'Geração Alpha'
    END AS Geracao,
    CASE
        WHEN EXTRACT(YEAR FROM data_nascimento) BETWEEN 1925 AND 1940 THEN '1925 a 1940'
        WHEN EXTRACT(YEAR FROM data_nascimento) BETWEEN 1941 AND 1959 THEN '1941 a 1959'
        WHEN EXTRACT(YEAR FROM data_nascimento) BETWEEN 1960 AND 1979 THEN '1960 a 1979'
        WHEN EXTRACT(YEAR FROM data_nascimento) BETWEEN 1980 AND 1995 THEN '1980 a 1995'
        WHEN EXTRACT(YEAR FROM data_nascimento) BETWEEN 1996 AND 2010 THEN '1996 a 2010'
        ELSE '2010 até dias atuais'
      END AS Periodo_nascimento,
    SUM(ROUND(r.Rake,2)) AS Total_Rake
FROM
    `sapient-tractor-310701.H2Club.resultado` r
JOIN
    `sapient-tractor-310701.H2Club.clientes` c ON r.Clientes_id = c.Id
GROUP BY
    Geracao,
    Periodo_nascimento;