
## Patrón Prototype:

Es un patrón de diseño creacional que nos permite copiar objetos existentes sin hacer
que el código dependa de sus clases.

Es útil cuando queremos duplicar el contenido, 
el título y el autor de un documento, por ejemplo o cualquier objeto complejo.

https://refactoring.guru/es/design-patterns/prototype


El patrón Prototype sirve para crear nuevos objetos copiando (clonando) una instancia existente, en lugar de crearlos desde cero usando new.

Es un patrón creacional y se usa cuando crear un objeto es costoso, complejo o repetitivo, o cuando querés evitar acoplar el código a clases concretas.

Idea principal (en simple)
“En vez de construir un objeto desde cero, hago una copia de uno que ya existe.”

¿Qué problema resuelve?

- Objetos complejos de crear
    - Mucha configuración
    - Carga de datos
    - Dependencias internas
- Necesidad de muchas instancias similares
    - Cambian pocos valores entre una y otra
- Evitar new y lógica de construcción repetida
    - El código cliente no conoce los detalles de construcción

Estructura básica:
- Prototype: interfaz o clase base con el método clone()
- ConcretePrototype: implementa la clonación
- Client: usa clone() en vez de new