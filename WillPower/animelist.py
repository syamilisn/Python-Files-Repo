from anime import anime
#from file import class
anime1=anime("Black Clover","Magic",9.7,True)
anime2=anime("Sword Art Online","RPG",3.2,False)
#anime objects is created
print(anime1.name,anime1.genre,anime1.imdb,anime1.success)
print(anime2.name,anime2.genre,anime2.imdb,anime2.success)
print(anime1.name,"is",anime1.hit())
print(anime2.name,"is",anime2.hit())