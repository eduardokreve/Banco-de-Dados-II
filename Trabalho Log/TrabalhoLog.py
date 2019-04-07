# coding=utf-8
import os
import string

def files(nomeArquivo):
    try:
        file = open(nomeArquivo, 'r')
        print("Arquivo encontrado") 
    except:
        print("Arquivo não encontrado")
        main()
    finally:
        
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
    nomeArquivo = input("Nome do arquivo: ")

    tabelaDeLog = files(nomeArquivo)
    i = 0

    while i < len(tabelaDeLog):
        print(tabelaDeLog[i])
        i += 1

if __name__ == "__main__":
    main()
