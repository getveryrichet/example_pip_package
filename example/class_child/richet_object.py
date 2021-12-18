from random import randint



class RichetObject:
    def __init__(self, name):
        self.name = name 
        

    def print_name(self):
        for i in range(randint(1, 3)):
            print(self.name)