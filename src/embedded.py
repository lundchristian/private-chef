# pylint: skip-file


class RaspberryPi:

    def get_fridge_contents(self):
        path = "documents/food_items_1.txt"
        with open(path, "r") as file:
            fridge_contents = file.read()
        return fridge_contents
