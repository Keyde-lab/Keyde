USE trabalho_banco;

-- Objetivo: Contar quantos clientes existem por país
SELECT country, COUNT(*) AS total_clientes
FROM customers
GROUP BY country;
