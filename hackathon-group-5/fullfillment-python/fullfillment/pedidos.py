from dataclasses import dataclass
from datetime import date
from typing import List
from enum import Enum

@dataclass
class Produto():
    codigo: int
    tipo: str
    nome: str

class StatusEntrega(Enum):
    EMPRESA = 1
    TRANSPORTADORA = 2
    ENTREGUE = 3

@dataclass
class Pedido():
    codigo: int
    data: date
    entrega: StatusEntrega

PEDIDOS = [
    Pedido(112233, date(2019, 8, 2), StatusEntrega.EMPRESA),
    Pedido(222222, date(2017, 8, 2), StatusEntrega.ENTREGUE),
    Pedido(999999, date(2019, 10, 12), StatusEntrega.ENTREGUE),
]