
SELECT * FROM codae_publicaciones AS pub 
LEFT JOIN codae_contenido AS ct 
ON pub.id=ct.id_publi
LEft JOIN codae_nivel_1 AS n_1
ON pub.id=n_1.id_publi
LIMIT 10;

