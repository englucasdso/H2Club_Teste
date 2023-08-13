#tabela referenciada com Common Table Expression
WITH TotalGanhadores AS (
    SELECT
        COUNT(DISTINCT r.clientes_id) AS Total
    FROM
        `sapient-tractor-310701.H2Club.resultado` r
    WHERE
        r.Winning > 0
)

#consulta principal
SELECT
    c.Sexo,
    COUNT(DISTINCT r.clientes_id) AS Numero_Ganhadores,
    ROUND(100 * COUNT(DISTINCT r.clientes_id) / Total, 0) AS Percentual
FROM
    `sapient-tractor-310701.H2Club.resultado` r
JOIN
    `sapient-tractor-310701.H2Club.clientes` c ON r.clientes_id = c.id
CROSS JOIN
    TotalGanhadores
WHERE
    r.Winning > 0
GROUP BY
    c.Sexo, Total


#adicao da linha total
UNION ALL

SELECT
    'Total' AS Sexo,
    COUNT(DISTINCT r.clientes_id) AS Numero_Ganhadores,
    100.00 AS Percentual
FROM
    `sapient-tractor-310701.H2Club.resultado` r
WHERE
    r.Winning > 0
ORDER BY 
    Percentual desc;

