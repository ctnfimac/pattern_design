CREATE TABLE automovil(
    marca varchar NOT NULL, 
    modelo varchar NOT NULL, 
    motor varchar NOT NULL, 
    color char(6) default "FFFFFF", 
    precio float NOT NULL    
);

-- DROP TABLE automovil;

INSERT INTO automovil(marca,modelo,motor,color,precio) 
VALUES ('Volkswagen','Polo','1.6','Blanco',5000000);  

INSERT INTO automovil(marca,modelo,motor,color,precio) 
VALUES ('Toyota','Yaris','1.4','Rojo',7000000);  

-- SELECT * FROM automovil;

--DROP TABLE automovil;

--SELECT rowid, * from automovil;