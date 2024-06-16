from .dog import Dog
from .adopter import Adopter
from .adoption import Adoption

# Create tables
Dog.create_table()
Adopter.create_table()
Adoption.create_table()
