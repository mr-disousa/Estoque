from dataclasses import dataclass

from src.models.contact import Contact


@dataclass
class Supplier:
    name: str
    contact: Contact
    cnpj: str

