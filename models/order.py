from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
    number_of_order: int
    items: []
    date_of_order: datetime
    value_of_order: float
    paymment_method: str


