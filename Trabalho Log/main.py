# coding=utf-8
import os
import string
from arquivo import openFile, clearLista,imprimeLista

#definição da classe para utilizar Lista de Objetos
class Transacao:
    def __init__(self, nome, var):
        self.Ti: nome
        self.var: var
        self.old: int = 0
        self.new: int = 0

class Ckpt:
    def __init__(self, inicio, transacao):
        self.inicioCkpt = inicio
        self.fimCkpt = 0
        self.transacao = transacao
    

def main ():
    tabelaDeLog = openFile() #abre
    clearLista(tabelaDeLog)  #limpa
    imprimeLista(tabelaDeLog)#mostra na tela

    ini = Transacao('t1', 'A')
    
    objetoCkpt= Ckpt(2,ini)
    print(objetoCkpt.transacao)


if __name__ == "__main__":
    main()
