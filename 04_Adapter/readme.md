# Patrón Adapter

Es un patrón de diseño estructural el cual permite que dos objetos con interfaces incompatibles puedan colaborar juntas. Es como un intermediario entre dos objetos.

Este patrón sirve para hacer compatibles dos objetos con interfaces distintas, como analogía se podria dar el ejemplo de un transformador que entrega una corriente
continua de 12volt y se tiene que alimentar una placa electrónica que trabaja con 3volt entonces utilizo un driver(adaptador) que lleve ese voltaje de 12 a 3 volt

Separa la lógica de conversion de datos de la lógica de negocio o lógica de aplicación (principio de unica responsabilidad)

se puede añadir nuevos adaptadores sin alternar la funcionalidad existente (principio de abierto o cerrado)


![observer5](https://github.com/user-attachments/assets/1f520cc7-5876-4f5d-a1e0-9e2faf42f8e4)