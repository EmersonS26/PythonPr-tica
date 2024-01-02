lista_de_compras = ["Batata","Cebola","Carne","Café","Leite","Biscoito"]
print(lista_de_compras.append("Açucar")) #adicionando um item a lista


print(lista_de_compras[0:])
print("Essa lista contém:",len(lista_de_compras)," Itens dos quais...\n")


print("vegetais: ", lista_de_compras[0:2]) #função slice em python,onde pega a posição de um elemento inicial da lista(0-Batata) até outro e exclui o ultimo indice(2-carne)

print("Não liquidos e não vegetais: ", lista_de_compras[2::3])#aqui utilizei os 2 pontos(::) 2x para indicar que ele comece de carne(posição 2) e pule de 2 em 2(café e leite) para chegar em Biscoito.

print("Liquidos: ", lista_de_compras[3:5],"\n")

print("1kg de:",lista_de_compras[2])#pegando o item,utilizando a posição dele
print("2kg de:",lista_de_compras[0])
print("3kg de:",lista_de_compras[1])
print("1 pacote de:",lista_de_compras[3])
print("2 pacotes de:",lista_de_compras[5])
print("1L(litro) de:",lista_de_compras[4])


print("Batata" in lista_de_compras)# batata está na lista de compras? TRUE(verdadeiro ou verdade) batata está na lista de compras

nome_loja = [
    ["cea","riachuelo","renner"],
    ["kalunga","gbarbosa","lojas americanas"],
    ["nike","adidas","puma"]
]

print(nome_loja[2][0]) #pegando a linha 2(3 linha) e coluna 0(nike) da 3 linha
