nome_cidades = {
    "Nome" : "Salvador",
    "Estado" : "Bahia",
    "Região" : "Nordeste"
}

nome_cidades["Pais"] = "Brasil" #adicionando elementos no dicionário

nome_cidades["Região"] = "Nordestde Amaralina" #Trocando o valor de um elemento,antes era Nordeste e eu troquei para Nordeste de Amaralina

print(nome_cidades["Estado"])#acessando um único valor,nesse caso acessando Estado que retorna Bahia

print(nome_cidades.keys())#retorna apenas as chaves do dicionario ex: "Nome" :
print(nome_cidades.values())#retorna apenas os valores do dicionario
print(nome_cidades.items())# retorna as chaves e valores do dicionario dentro de parenteses de forma organizada.