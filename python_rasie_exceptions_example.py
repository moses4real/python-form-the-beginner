class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_Coffee(self):
        if self.__temperature > 85:
            #print('Coffee Too Hot')
            raise Exception ('Coffee Too Hot')
        elif self.__temperature < 65:
            #print('Coffee Too Cold')
            raise ValueError('Coffee Too Cold')
        else:
            print('Coffee ok to Drink')

cup = CoffeeCup(10)
cup.drink_Coffee()