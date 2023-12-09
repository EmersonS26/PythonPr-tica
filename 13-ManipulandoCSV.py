import csv #importando a biblioteca para abrir arquivo csv

with open("coord_predio_vertices.csv","r",encoding="utf-8") as arquivo_csv:#abrir arquivo
    leitor = csv.reader(arquivo_csv)#fazer a leitura do arquivo
    for linha in leitor:#percorre as linhas com o conteudo dentro do arquivo
        print(linha)
        

with open("coord_predio_vertices.csv","w",encoding="utf-8") as escrita:
    escrita1 = csv.writer(escrita)
    escrita1.writerow(["tomate", "cebola"])
    print(escrita1)
    

        
    