# Patrón Observer

Es un patrón de diseño de comportamiento que te permite definir un mecanismo de suscripción para notificar a varios objetos sobre cualquier evento que le suceda al objeto que están observando.

Cuando un objeto cambia de estado todos sus dependientes son notificados automáticamente. Ejemplo: un sistema de noticias en donde el periódico publica noticias y los lectores (subscriptores) se mantienen informados sobre las nuevas publicaciones. El periódico actúa como el Sujeto y los suscriptores como los Observadores

![Observer4](https://github.com/user-attachments/assets/24aa7514-765a-49f6-9916-e1bef3d6946b)

copiar el archivo .env_ a uno .env y completar los campos con las credenciales del email
personal

### Estructura del proyecto
```
01_ObserverPattern/
│
├── app/
│   │
│   │
│   ├── src/                           
│   │   ├── models/                    
│   │   │    ├── Automovil.py              
│   │   │    ├── Database.py
│   │   │ 
│   │   ├── pattern/  
│   │   │    ├── observer/
│   │   │    │    ├── base/
│   │   │    │    │    ├── patron_observador.py 
│   │   │    │    ├── email/
│   │   │    │    │    ├── email_subject.py 
│   │   │    │    │    ├── suscriptor_automovil_crud.py
│   │   │  
│   │   ├── __init__.py
│   │
│   │
│   ├── db/                         
│   │   ├── test.db                    
│   │   ├── test.sql             # Sql para crear la tabla y guardar dos registros 
│   │
│   ├── main.py                  # Punto de entrada de la aplicación 
│
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Descripción del proyecto
```


#### Referencias:
https://refactoring.guru/es/design-patterns/observer
https://stackoverflow.com/questions/64505/sending-mail-from-python-using-smtp (para el envio de email)



