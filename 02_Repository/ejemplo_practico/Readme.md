# Patron Repository

Se utiliza para separar la aplicación del almacenamiento de datos funcionando como un mediador entre ambos. 
El repositorio proporciona un conjunto de métodos para realizar operaciones CRUD

![repository](https://github.com/user-attachments/assets/335a2fd2-d230-44bd-99c8-20f7140c24de)


Uno de sus objetivos es separar la capa de lógica de negocio con 
la capa de datos, esto tiene como ventaja por ejemplo si estoy trabajando con una base de datos postgres y la tengo que cambiar por una mysql no tengo que modificar el código de la capa de lógica negocio.


### Estructura del proyecto
```
project_root/
│
├── app/
│   ├── api/                         # Endpoints y rutas
│   │   ├── v1/                      # Versionado de la API
│   │   │   ├── endpoints/           # Controladores o puntos finales de la API
│   │   │   │   ├── club_api.py      # Ejemplo: endpoints de club
│   │   │   │   ├── jugador_api.py   # Ejemplo: endpoints de jugador
│   │   │   ├── __init__.py
│   │   ├── __init__.py
│   │
│   ├── db/                          # Capa de base de datos y conexión
│   │   ├── base.py                  # Declaración de clases base para SQLAlchemy
│   │   ├── __init__.py
│   │
│   ├── models/                      # Modelos de base de datos
│   │   ├── club.py                  # Modelo de club (SQLAlchemy o Pydantic)
│   │   ├── jugador.py               # Modelo de ejemplo para jugadores
│   │   ├── __init__.py
│   │
│   ├── repositories/                # Implementaciones de repositorios
│   │   ├── club_repository.py       # Repositorio para el modelo de Club
│   │   ├── jugador_repository.py    # Repositorio para el modelo de Jugador
│   │   ├── __init__.py
│   │
│   ├── services/                    # Lógica de negocio o capa de servicio
│   │   ├── club_service.py          # Servicios relacionados con clubes
│   │   ├── jugador_service.py 
│   │   ├── __init__.py
│   │
│   ├── schemas/                     # Esquemas Pydantic (validación de datos)
│   │   ├── club_schemas.py          # Esquemas de entrada y salida para clubes
│   │   ├── jugador_schema.py        # Esquemas para jugadores
│   │   ├── __init__.py
│   │
│   ├── main.py                      # Punto de entrada de la aplicación (FastAPI)
│   ├── __init__.py
│
├── requirements.txt                 # Dependencias del proyecto
└── README.md                        # Descripción del proyecto
```

### Creación de base de datos de prueba

Para el segundo ejemplo del patrón repository se ve como se cambia fácilmente de una base
de datos SQlite a una Postgresql sin necesitad de modificar el código de la lógica de negocio.

Creación de la base de datos postgres con docker:
```
docker run -d --name repositorydb -p 3009:5432 -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=christian -e POSTGRES_DB=repositorydb  postgres
```
Para conectarse desde un cliente psql
```
psql -h localhost -p 3009 -U christian -d repositorydb
```



### Fuentes:
- https://www.youtube.com/watch?v=b2tPRbQJing
- https://www.youtube.com/watch?v=vMVEYC-rTeQ
- https://www.youtube.com/watch?v=QqsH0OgqafA
- https://platzi.com/blog/patron-repository/
