# Patrón Builder 

Este Patrón de diseño creacional sirve para construir objetos complejos
de manera controlada y paso a paso, o sea que pueden tomar distintas formas dependiendo la necesidad del cliente. 
Por ejemplo si quiero construir una casa puede que quiera una con piscina, otra que no tenga patio, otra que tenga garage, una con porton electrico etc.

Si bien se podria crear una sola clase y que tenga un constructor
con muchos parámetros esto no es muy elegante en el código y lo hace poco mantenible en el tiempo.


![structure-indexed](https://github.com/user-attachments/assets/33f0278f-d9d2-4de1-b8d1-0391606e6d68)

#### Propósito:
- Separar la construcción de un objeto de su representación para que el mismo proceso de construcción pueda crear diferentes representaciones.
- Facilitar la creación de objetos complejos evitando que el constructor principal tenga demasiados parámetros o que el código de construcción se vuelva difícil de leer y mantener.

#### Componentes del Patrón Builder
- **Builder**: Define la interfaz para crear partes del objeto.
- **ConcreteBuilder**: Implementa la interfaz de Builder y construye partes específicas del producto.
- **Director**: Dirige el proceso de construcción mediante el uso del Builder.
- **Product**: El objeto complejo que se construye.

### Estructura del proyecto
```
03_Builder/
│
├── app/
│   │
│   │
│   ├── clases/                            # Clases del proyecto
│   │   ├── builder_form/                  # Clases para la construcción
│   │   │    ├── builder.py                # de formularios.
│   │   │    ├── form_builder_director.py
│   │   │    ├── form_item.py
│   │   │    ├── login_builder.py
│   │   │    ├── recover_builder.py
│   │   │    ├── register_builder.py
│   │   │    ├── __init__.py
│   │   ├
│   │   ├── __init__.py
│   │
│   │
│   ├── templates/                         # Capa de presentación
│   │   ├── index.html                     # Página que muestra los formularios
│   │
│   ├── main.py                            # Punto de entrada de la aplicación (Flask)
│   ├── __init__.py
│
├── requirements.txt                       # Dependencias del proyecto
└── README.md                              # Descripción del proyecto
```


#### Fuentes:
https://www.youtube.com/watch?v=zfW9uEoGx2c&list=PL9q8JzvoZPi_4_CcKEz5Q3otNztY_25ia&index=29
https://medium.com/@amirm.lavasani/design-patterns-in-python-builder-0732552324b1
