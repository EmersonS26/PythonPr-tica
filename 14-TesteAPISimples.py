import requests #importando biblioteca request, que para instalar é só dar um: pip install requests.  no terminal.

url = 'https://api.exchangerate-api.com/v6/latest'#definindo a url e declarando o endereço

req = requests.get(url)#fazendo a requisição com o metodo GET

dados = req.json()#estrutura de dados json
#print(req.status_code) verifica se o status está ok

valor_reais = float(input("Informe o valor em reais a ser cnvertido: "))

cotacao = dados['rates']['BRL']
print(f'{valor_reais} em dólar valem US$ {(valor_reais / cotacao):.2f}')
