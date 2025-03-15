class Lista:
    def __init__(self, lista = ["banana", "uva", "laranja", "abacaxi", "morango"]):
        self.lista = lista 
        
    def inverteLista(self):
        return self.lista[::-1] 
    
print(Lista().inverteLista())