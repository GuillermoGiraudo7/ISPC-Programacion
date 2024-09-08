CREATE DATABASE pulidoradb;
USE pulidoradb;
CREATE TABLE lentes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estado ENUM('apagada', 'encendida') NOT NULL,
    velocidad INT NOT NULL,
    modo ENUM('básico', 'avanzado', 'ultra') NOT NULL,
    nivel_lente DECIMAL(5, 2) NOT NULL
);
INSERT INTO lentes (estado, velocidad, modo, nivel_lente) VALUES
('encendida', 20, 'básico', 10.50),
('apagada', 0, 'básico', 0.00),
('encendida', 50, 'avanzado', 7.25),
('encendida', 30, 'ultra', 3.75),
('apagada', 0, 'básico', 5.00),
('encendida', 60, 'avanzado', 8.00),
('encendida', 45, 'ultra', 2.50),
('apagada', 0, 'básico', 4.25),
('encendida', 35, 'avanzado', 6.00),
('encendida', 25, 'ultra', 9.00);

SELECT*FROM lentes;

SELECT*FROM lentes WHERE estado='encendida';

SELECT*FROM lentes WHERE velocidad>30;

SELECT*FROM lentes WHERE modo='avanzado' AND nivel_lente<7;

SELECT estado, COUNT(*) AS cantidad FROM lentes GROUP BY estado;