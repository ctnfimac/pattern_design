# Aprendiendo Patrones de Diseño

### 1) Patrón Observador
El ejemplo es un crud de una clase automovil, en donde se informará mediante el envio
de email de las 4 operaciones a los distintos suscriptores que se registran con su correo electrónico corporativo.
Al mismo tiempo se informará por medio del sistema Slack a los suscriptores que esten suscritos con su respectiva key.

### 2) Patrón Repository
Para este patrón se deja un ejemplo de una api para crear y obtener datos realizada con FastApi en el cual el proyecto inicia utilizando una base de datos **Sqlite** con el orm SQLAlchemy, en la siguiente etapa se utiliza una base de datos **Postgres** en donde se deja en evidencia el mínimo de modificaciones solo en el código de la configuración, y por último se cambia al uso de una base de datos **Mysql** sin orm en donde también se modifica la configuración, se deja de usar modelos(ya que no se usa el orm) y se modifica el código de los repositorios. En conclusión no se modifico el código de la lógica de negocio que es a donde apunta el patron.


### 2) Patrón Builder
Para este patrón dejo un ejemplo de formularios de Login, Registro y Recuperar contraseña.
Dependiendo cual necesite lo construyo y muestro en pantalla
