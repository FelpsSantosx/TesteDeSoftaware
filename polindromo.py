class Polindromo:
    def __init__(self, palavra):
        self.palavra = palavra
        
    def eh_polindromo(self):
        palavra = self.palavra.replace(' ', '').lower()
       
        return palavra == palavra[::-1]
        
print(Polindromo('ovo').eh_polindromo())
print(Polindromo('banana').eh_polindromo())
print(Polindromo('Ame a ema').eh_polindromo())
print(Polindromo('A sogra má e amargosa').eh_polindromo())
print(Polindromo('Ame o poema').eh_polindromo())
print(Polindromo('python').eh_polindromo())
print(Polindromo('arara').eh_polindromo())
print(Polindromo('radar').eh_polindromo())