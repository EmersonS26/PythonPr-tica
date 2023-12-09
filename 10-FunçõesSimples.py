def calcular(valor1,valor2):
    valores = valor1 * valor2
    return valores


resultado = calcular(23,27)

print(resultado)

def exemplo1(*valores):#vários valores em um unico parametrodentro da funcao
    print(valores)
    
exemplo1(1,2,3)   


def dicionario(**dict):
    print(dict, type(dict))
    
dicionario(nome = "carlão da massa", profissao = "jogador de comida profissiona")    



def nome(name,idade):
    name : name
    idade : idade
    return name, idade

nomes = nome("camila",23)

print(nomes)