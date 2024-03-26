from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    name: str
    size_in_cm: float
    weight_in_kg: float
    color: str
    price: float
    validate: datetime
    quantity: int
    brand: str
    batch: str
    bar_code: str


