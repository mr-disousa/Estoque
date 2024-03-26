from dataclasses import dataclass

from src.models.contact import Contact


@dataclass
class Customer:
    name: str
    contact: Contact
    order: []


