USE trabalho_banco;

INSERT INTO customers (first_name, last_name, country) VALUES
('Ana', 'Silva', 'Brazil'),
('João', 'Souza', 'Brazil'),
('Maria', 'Oliveira', 'USA'),
('Carlos', 'Lima', 'USA'),
('Pedro', 'Santos', 'Portugal');

INSERT INTO invoices (customer_id, total, billing_country) VALUES
(1, 50.00, 'Brazil'),
(1, 30.00, 'Brazil'),
(2, 20.00, 'Brazil'),
(3, 100.00, 'USA'),
(4, 70.00, 'USA'),
(5, 40.00, 'Portugal');

SELECT * FROM customers;

INSERT INTO artists (name) VALUES 
('Legião Urbana'),
('Titãs');

INSERT INTO albums (title, artist_id) VALUES 
('Dois', 1),
('Cabeça Dinossauro', 2);

INSERT INTO tracks (name, album_id) VALUES 
('Tempo Perdido', 1),
('Eduardo e Mônica', 1),
('AA UU', 2),
('Bichos Escrotos', 2);

SELECT * FROM invoices;