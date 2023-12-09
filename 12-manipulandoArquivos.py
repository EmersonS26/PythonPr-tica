arquivo = open("arquivo1.txt","r",encoding="utf-8")#BLOCO DE CODIGO P/ ABRIR UM ARQUIVO(JEITO COMPLEXO) UTILIZA O CLOSE)
texto = arquivo.read()
print(texto)
arquivo.close()


#EXISTE UMA BOA PRÁTICA E JEITO MAIS FÁCIL DE ABRIR UM ARQUIVO EM PYTHON ABAIXO:

with open("arquivo1.txt","r", encoding="utf-8") as arquivox:#NESSE EXEMPLO A ESTRUTRA JÁ FECHA O ARQUIVO AUTOMATICAMENTE
    texto = arquivox.read()
    print(texto)
    

#CRIANDO UM ARQUIVO EM PYTHON:

with open("Novoarquivo.txt","w",encoding="utf-8") as arquivo:
    arquivo.write("Aqui é onde escrevo o conteúdo do meu novo arquivo...")
    arquivo.write("Posso escrever quantas vezes eu quiser desde que siga as regras...\n")     
