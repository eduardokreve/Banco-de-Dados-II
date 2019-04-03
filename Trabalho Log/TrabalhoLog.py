# coding=utf-8
import string

def imprime(fita, pos, i):
    q = ["q0         ","qli_um     ","qteste_um  ","q_         ",
    "qli_zero   ", "qteste_zero", "qsim       ","qnao       "]

    print("(", q[i], " | ", *fita, " cabeça=>",pos, ")", sep="")

def qteste_zero(fita, pos): #pronto
    i = 5
    if fita[pos] == ">":
        imprime(fita, pos, i)
        imprime(fita, pos, 6) 
    elif fita[pos] == "0":
        fita[pos] = ":" 
        pos -=1
        imprime(fita, pos, i)
        q_(fita, pos)
    elif fita[pos] == "1":
        imprime(fita, pos, i)
        imprime(fita, pos, 7)
    
def qli_zero(fita, pos): #pronto
    i = 4
    if fita[pos] == "0":
        pos +=1
        imprime(fita, pos, i)
        qli_zero(fita, pos)
    elif fita[pos] == "1":
        pos +=1
        imprime(fita, pos, i)
        qli_zero(fita, pos)
    elif fita[pos] == ":":
        pos -=1
        imprime(fita, pos, i)
        qteste_zero(fita, pos)

def q_(fita, pos): #pronto 
    i = 3 
    if fita[pos] == ">":
        pos +=1
        imprime(fita, pos, i)
        q0(fita, pos)
    elif fita[pos] == "0":
        pos -=1
        imprime(fita, pos, i)
        q_(fita, pos)
    elif fita[pos] == "1":
        pos -=1
        imprime(fita, pos, i)
        q_(fita, pos)

def qteste_um(fita, pos): #pronto
    i = 2
    if fita[pos] == ">":
        imprime(fita, pos, i)
        imprime(fita, pos, 6) 
    elif fita[pos] == "0":
        imprime(fita, pos, i)
        imprime(fita, pos, 7)
    elif fita[pos] == "1":
        fita[pos] = ":"
        pos -=1
        imprime(fita, pos, i)
        q_(fita, pos)

def qli_um(fita, pos): #pronto
    i = 1
    if fita[pos] == "0":
        pos +=1
        imprime(fita, pos, i)
        qli_um(fita, pos)
    elif fita[pos] == "1":
        pos +=1
        imprime(fita, pos, i)
        qli_um(fita, pos)
    elif fita[pos] == ":":
        pos -=1
        imprime(fita, pos, i)
        qteste_um(fita, pos)

def q0(fita, pos): #pronto
    i = 0
    if fita[pos] == ">":
        pos +=1
        imprime(fita, pos, i)
        q0(fita, pos)
    elif fita[pos] == "0":
        fita[pos] = ">"
        pos +=1
        imprime(fita, pos, i)
        qli_zero(fita, pos)
    elif fita[pos] == "1":
        fita[pos] = ">"
        pos +=1
        imprime(fita, pos, i)
        qli_um(fita, pos)
    elif fita[pos] == ":":
        imprime(fita, pos, i)
        imprime(fita, pos, 6) 

def invalido(x): #verifica se é somente 0 e 1
    carac = "23456789"
    i = 0
    while i < len(x):
        if (x[i] in carac) == True:
            return True
        i += 1 
    return False

def main():
    fita = [":" for x in range(30)] #preenche a fita com o simbolo de final -> (:) 
    fita[0] = ">" #marca o inicio
    
    x = input("Entre com a cadeia binaria: ")

    if (x.isnumeric()) != True: #verifica se nao é vazio e se são numeros
        main()
    elif (invalido(x)) == True:
        main()
    else:
        indice = 0
        pos = 1
        #coloca a cadeia binaria na fita
        while indice <len(x):
            fita[pos] = x[indice]
            pos += 1
            indice += 1
        
        imprime(fita, 1, 0) #imprime a fita antes de computar
        #print(fita)
        #primeira chamada de função para verificar
        q0(fita, 1) #fita, posição da cabeça 

if __name__ == "__main__":
    main()  