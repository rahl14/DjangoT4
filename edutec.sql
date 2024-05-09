-- Crear la base de datos
CREATE DATABASE edutec;

-- Usar la base de datos edutec
USE edutec;

-- Crear la tabla Alumno
CREATE TABLE IF NOT EXISTS Alumno (
    id_alumno INT AUTO_INCREMENT PRIMARY KEY,
    nombre_apellido VARCHAR(100),
    nombre_curso VARCHAR(50),
    nota_curso FLOAT,
    estado VARCHAR(20)
);

DELIMITER //

CREATE PROCEDURE sp_crear_alumno(
    IN p_nombre_apellido VARCHAR(100),
    IN p_nombre_curso VARCHAR(50),
    IN p_nota_curso FLOAT
)
BEGIN
    INSERT INTO Alumno (nombre_apellido, nombre_curso, nota_curso, estado)
    VALUES (p_nombre_apellido, p_nombre_curso, p_nota_curso,
            CASE WHEN p_nota_curso >= 14 THEN 'Aprobado' ELSE 'Desaprobado' END);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE sp_actualizar_alumno(
    IN p_id_alumno INT,
    IN p_nombre_apellido VARCHAR(100),
    IN p_nombre_curso VARCHAR(50),
    IN p_nota_curso FLOAT
)
BEGIN
    UPDATE Alumno
    SET nombre_apellido = p_nombre_apellido,
        nombre_curso = p_nombre_curso,
        nota_curso = p_nota_curso,
        estado = CASE WHEN p_nota_curso >= 14 THEN 'Aprobado' ELSE 'Desaprobado' END
    WHERE id_alumno = p_id_alumno;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE sp_eliminar_alumno(
    IN p_id_alumno INT
)
BEGIN
    DELETE FROM Alumno WHERE id_alumno = p_id_alumno;
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_obtener_alumno_por_id(
	IN p_id_alumno INT
)
BEGIN
    SELECT * FROM Alumno 
    WHERE id_alumno = p_id_alumno;
END //
DELIMITER ;

DELIMITER //

CREATE PROCEDURE sp_obtener_alumnos()
BEGIN
    SELECT * FROM Alumno;
END //

DELIMITER ;

-- Probando los procedimientos almacenados
    
CALL sp_crear_alumno('Juan Pérez', 'Matemáticas', 16);

CALL sp_crear_alumno('María García', 'Ciencias', 12);

CALL sp_crear_alumno('Luis Martínez', 'Historia', 18);

CALL sp_obtener_alumnos();


