# coding=utf-8
import os
import string
from dataclasses import dataclass

#definição da classe para utilizar Lista de Objetos
@dataclass
class Point:
    Ti: str
    var: str
    old: int = 0
    new: int = 0

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

    ini = Point('t1', 'A')

    print(ini)
    
if __name__ == "__main__":
    main()
