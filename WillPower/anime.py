#creating class
#self:refers to object
#parameters are passed into initialization functions
class anime:
    def __init__(self,name, genre, imdb,success):
        self.name=name
        self.genre=genre
        self.imdb=imdb
        self.success=success
        
    def hit(self):
        if self.imdb>=8.5:
            return "Super hit!!"
        else:
            return "Utter Flop!"