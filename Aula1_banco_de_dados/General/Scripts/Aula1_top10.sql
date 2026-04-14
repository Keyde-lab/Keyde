USE trabalho_banco;

-- Objetivo: Listar os 10 clientes que mais gastaram
SELECT c.customer_id, c.first_name, c.last_name, SUM(i.total) AS total_gasto
FROM customers c
JOIN invoices i ON c.customer_id = i.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_gasto DESC
LIMIT 10;