# coding=utf-8
import os
import string

#definição da classe para utilizar Lista de Objetos
class log():
    def __init__(self, Ti = ' ', var = '', old = 0, new = 0):
        self.Ti = Ti
        self.var = var
        self.old = old
        self.new = new

def files():
    #abre o arquivo com o nome correto
    while True:
        try:
            nomeArquivo = input("Nome do arquivo: ")
            file = open(nomeArquivo, 'r')
        except FileNotFoundError:
            print("Arquivo não encontrado\n")
        else:
            break
    
    #pega os dados do arquivo e coloca na lista
    lista = []
    listaAux = []

    while 1:
        linha = file.readline()
        if linha == "":
             break
        if linha[0] ==  '':
            continue
        
        #passa o conteudo para as listas
        listaAux = linha
        lista.append(listaAux)

    file.close()

    return lista


def main ():
    tabelaDeLog = files()
    i = 0

    while i < len(tabelaDeLog):
        print(tabelaDeLog[i])
        i += 1

    #primeira tentativa para organizar os dados em uma estrutura
    #Proximo passo, organizar tudo em um conjunto de objetos
    #talvez ajude https://aprendendo-computacao-com-python.readthedocs.io/en/latest/capitulo_15.html
    
    ini = log()

    print(ini.new, ini.old)
    
if __name__ == "__main__":
    main()
