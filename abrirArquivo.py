def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não existe.")


conteudo = abrir_arquivo("arquivo.txt")
if conteudo:
    print(conteudo)