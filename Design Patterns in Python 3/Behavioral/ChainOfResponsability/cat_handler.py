from pet_handler import PetHandler

class CatHandler(PetHandler):

    def handle(self, request):
        if request.request_type == "cats":
            print("Cat Handler")
        else:
            super().handle(request)