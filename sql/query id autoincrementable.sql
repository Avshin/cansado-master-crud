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





CREATE SEQUENCE secuencia_grados;

SELECT setval('secuencia_grados', (SELECT max(id_gacademico) FROM grados_academicos));

ALTER TABLE grados_academicos
ALTER COLUMN id_gacademico SET DEFAULT nextval('secuencia_grados');


UPDATE public.cargos
                SET  detalle_cargo='auxiliar'
                WHERE id_cargo=1;









