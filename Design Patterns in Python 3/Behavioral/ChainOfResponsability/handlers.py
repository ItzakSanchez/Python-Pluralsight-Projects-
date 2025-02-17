from pet_handler import PetHandler
from dog_handler import DogHandler
from cat_handler import CatHandler

handler_chain = PetHandler(None)
for handler in CatHandler, DogHandler:
    new_handler = handler(handler_chain)
    handler_chain = new_handler