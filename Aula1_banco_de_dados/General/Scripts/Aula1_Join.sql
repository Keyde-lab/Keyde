USE trabalho_banco;

SELECT t.name AS musica, a.title AS album, ar.name AS artista
FROM tracks t
JOIN albums a ON t.album_id = a.album_id
JOIN artists ar ON a.artist_id = ar.artist_id;

-- Objetivo: Listar compras feitas por clientes do Brasil
SELECT c.first_name, c.last_name, i.invoice_id, i.total
FROM customers c
JOIN invoices i ON c.customer_id = i.customer_id
WHERE c.country = 'Brazil';

