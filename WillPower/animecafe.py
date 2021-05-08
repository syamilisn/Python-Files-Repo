#inherit skilld from hotel chef to anime maid
from Inheritance import chef
class maidsama(chef):
    """def makechicken(self):
        print("Order: Chicken is done")
    def makesalad(self):
        print("Order: Salad is done")"""
    def makespecial(self):
        print("Order: anime-themed cocktail is done")
    def makecoffee(self):
        print("Order: Coffee is done")
    def makedessert(self):
        print("Order: Dessert is done")
    def makecake(self):
        print("Order: Cake is done")
        
"""When superclass and subclass are having functions with same name priotity is given to the subclass fn.
i.e. the fn of the subclass overrides the fn of the superclass with the same name."""