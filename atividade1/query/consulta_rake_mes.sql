SELECT
    EXTRACT(MONTH FROM data_acesso) AS Mes,
    EXTRACT(YEAR FROM data_acesso) AS Ano,
    CONCAT(CAST(EXTRACT(YEAR FROM data_acesso) AS STRING), '-', CAST(EXTRACT(MONTH FROM data_acesso) AS STRING)) AS Data,
    SUM(ROUND(Rake,2)) AS Total_Rake
FROM
    `sapient-tractor-310701.H2Club.resultado`
GROUP BY
    Ano, 
    Mes,
    Data
ORDER BY 
    Ano DESC,
    Mes DESC;