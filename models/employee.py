from dataclasses import dataclass

from src.models.contact import Contact


@dataclass
class Employee:
    name: str
    rg: str
    cpf: str
    code_employee: int
    contact: Contact
    contact_for_emergency: int
    uniform_size: str