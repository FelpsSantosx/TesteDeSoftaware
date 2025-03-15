class ContaOcorrencia:
    def __init__(self, texto):
        self.ocorrencias = {}
        self.texto = texto
        
    def contaOcorrencia(self):
        for letra in self.texto:
            if letra.isalpha():
                if letra in self.ocorrencias:
                    self.ocorrencias[letra] += 1
                else:
                    self.ocorrencias[letra] = 1

        return self.ocorrencias            

print (ContaOcorrencia('banana').contaOcorrencia())
print (ContaOcorrencia('eu amoo python').contaOcorrencia())