# coding=utf-8
import os
import string
from dataclasses import dataclass
from arquivo import openFile
from arquivo import clearLista

#definição da classe para utilizar Lista de Objetos
@dataclass
class Point:
    Ti: str
    var: str
    old: int = 0
    new: int = 0


def main ():
    tabelaDeLog = openFile()
    clearLista(tabelaDeLog) #limpar a lista
    i = 0

    while i < len(tabelaDeLog):
        print(tabelaDeLog[i])
        i += 1

    ini = Point('t1', 'A')

    print(ini)
    
if __name__ == "__main__":
    main()
