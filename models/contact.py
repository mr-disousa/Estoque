from dataclasses import dataclass

@dataclass
class Contact:
    tel: str
    email: str
    website: str
    address: str
    city: str
    state: str
    country: str