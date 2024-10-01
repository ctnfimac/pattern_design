from src.pattern.observer.base.patron_observador import Subject
from src.pattern.observer.base.patron_observador import Observer
from typing import List

#Observer
class SlackSubject(Subject):

    def __init__(self):
        self.suscriptores: List[Observer] = []
        self._accion_crud: str = ''

    def agregar_suscriptor(self, suscriptor:Observer) -> None:
        self.suscriptores.append(suscriptor)

    def eliminar_suscriptor(self, suscriptor:Observer) -> None:
        self.suscriptores.remove(suscriptor)
 
    def notificar_suscriptores(self) -> None:
        for suscriptor in self.suscriptores:
            suscriptor.update(self)

    def notificar_la_operacion(self, accion_crud: str) -> None:
        self._accion_crud = accion_crud
        print(f'Se realizo la operación {accion_crud} en la base de datos.')
        self.notificar_suscriptores()

