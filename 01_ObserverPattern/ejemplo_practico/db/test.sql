CREATE TABLE automovil(
    id integer PRIMARY KEY, 
    marca varchar NOT NULL, 
    modelo varchar NOT NULL, 
    motor varchar NOT NULL, 
    color char(6) default "FFFFFF", 
    precio float NOT NULL    
);

-- DROP TABLE automovil;

INSERT INTO automovil(id, marca,modelo,motor,color,precio) 
VALUES (1, 'Volkswagen','Polo','1.6','Blanco',5000000);  

INSERT INTO automovil(id, marca,modelo,motor,color,precio) 
VALUES (2, 'Toyota','Yaris','1.4','Rojo',7000000);  

-- SELECT * FROM automovil;