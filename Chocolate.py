class Chocolate :
    def __init__(self, sabor, preco = 5):
        self.sabor = sabor
        self.__preco = preco


    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        self.__preco = preco

    def altera_preco(self, preco):
        self.__preco = preco


chocolate1 = Chocolate('branco')
print(chocolate1.sabor)
