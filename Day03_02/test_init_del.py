class Dog:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def act(self):
        print('dog can eat bone')

    def getname(self):
        print('dog`s name is ',self.__name)

    def getage(self):
        print('dog`s age is',self.__age)



zhao=Dog('zhaozhao',12)
zhao.getage()
zhao.getname()
zhao.act()
del zhao