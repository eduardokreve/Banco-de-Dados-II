def openFile():
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

    while True:
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

def clearLista(lista):
    i = 0
    while i < len(lista):
        lista[i] = lista[i].lower() #coloca as letras para minusculo     
        lista[i] = lista[i].replace('<',"") #tira caracteres desnecessarios
        lista[i] = lista[i].replace('>',"")
        i+=1