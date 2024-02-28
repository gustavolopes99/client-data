from modules import *


class Validate():
    def validate_entry_cod(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100
