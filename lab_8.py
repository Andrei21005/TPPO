from __future__ import annotations
from abc import ABC, abstractmethod

class State_Automat(ABC):
    @abstractmethod
    def handle(self, context: Automat) -> None:
        pass

class State_Wait_Money(State_Automat):
    def handle(self, context: Automat) -> None:
        print("Ожидание оплаты, переход к выбору")
        context.state = State_Wait_Choise()

class State_Wait_Choise(State_Automat):
    def handle(self, context: Automat) -> None:
        print("Ожидание выбора, переход к выдаче")
        context.state = State_Get_Product()

class State_Get_Product(State_Automat):
    def handle(self, context: Automat) -> None:
        print("Выдача продукта, переход к дальнейшей оплате")
        context.state = State_Wait_Money()

class Automat:
    def __init__(self, state: State_Automat) -> None:
        self._state = state

    @property
    def state(self) -> State_Automat:
        return self._state

    @state.setter
    def state(self, state: State_Automat) -> None:
        self._state = state

    def request(self) -> None:
        self._state.handle(self)

if __name__ == "__main__":
    context = Automat(State_Wait_Money())
    context.request()
    context.request()
    context.request()
