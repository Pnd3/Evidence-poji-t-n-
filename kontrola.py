
class Kontrola():

    def cisla(num):
        try:
            float(num)
            return True
        except ValueError:
            return False
