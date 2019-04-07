# coding=utf-8
import os
import string

def files():
    
    while True:
        try:
            nomeArquivo = input("Nome do arquivo: ")
            file = open(nomeArquivo, 'r')
        except FileNotFoundError:
            print("Arquivo não encontrado\n")
        else:
            break
    
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

if __name__ == "__main__":
    main()
