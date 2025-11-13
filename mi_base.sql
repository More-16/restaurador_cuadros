CREATE DATABASE restauracion_cuatros;
use restauracion_cuatros;

CREATE TABLE Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    dni INT(8) ,
    numero INT(10),
)
CREATE TABLE Empledo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    fecha-de-nacimiento DATETIME,
    dni INT(8) ,
    numero INT(10),
)
CREATE TABLE CUADRO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Titulo VARCHAR(50) NOT NULL,
    autor VARCHAR(50) NOT NULL,
    año INT,
    altura INT,
    Ancho INT,
)
CREATE TABLE IF NOT EXISTS venta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    empleado_id INT,HJOP
    estado_actual VARCHAR(200),
    servicio VARCHAR(200),
    fecha_entrada DATETIME,
    fecha_entrega_estimada DATETIME,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id) ON DELETE SET NULL,
    FOREIGN KEY (empleado_id) REFERENCES empleado(id) ON DELETE SET NULL
);
