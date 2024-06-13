from .dog import Dog
from .adopter import Adopter
from .adoption import Adoption

# Drop existing tables if they exist
Dog.drop_table()
Adopter.drop_table()
Adoption.drop_table()

# Create tables
Dog.create_table()
Adopter.create_table()
Adoption.create_table()
