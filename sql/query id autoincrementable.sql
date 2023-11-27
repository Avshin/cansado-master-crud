-- 01) Crea una nueva secuencia en la base de datos:
CREATE SEQUENCE secuencia_cargos;

-- 02) Define un valor inicial para la secuencia
-- y asígnalo a la columna existente "id_personas"
-- en cada fila existente de la tabla "personas".

SELECT setval('secuencia_cargos', (SELECT max(id_cargo) FROM cargos));

-- 03) Modifica la definición de la columna "id_personas" 
-- para que tenga un valor por defecto tomado de la secuencia.

ALTER TABLE cargos
ALTER COLUMN id_cargo SET DEFAULT nextval('secuencia_cargos');





