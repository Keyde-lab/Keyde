USE trabalho_banco;

-- Objetivo: Mostrar países com vendas totais acima de 1000
SELECT billing_country, SUM(total) AS total_vendas
FROM invoices
GROUP BY billing_country
HAVING SUM(total) > 1000;