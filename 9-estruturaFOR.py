nome_cidade = ["Rio de Janeiro","Salvador","São Paulo"]

for nome in nome_cidade: #loop for que percorre cada palavra ou linha de 1 em 1
    print(nome)
    
nome_cidade1 = {
    "Nome" : "Cidade",
    "Cidade" : "São Paulo",
    "São Paulo" : "Estado"
}

for capital in nome_cidade1:
    print(f"{capital}:  {nome_cidade1[capital]}")  #chamando o dicionario em ordem com  o for,que percorre cada linha  
    
    