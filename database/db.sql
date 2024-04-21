CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo_electronico VARCHAR(100),
    contraseña VARCHAR(100),
    id_unico VARCHAR(100)
);

CREATE TABLE signos_vitales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    frecuencia_cardiaca INT,
    nivel_oxigeno INT,
    temperatura FLOAT,
    datos_acelerometro VARCHAR(100),
    datos_giroscopio VARCHAR(100),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
