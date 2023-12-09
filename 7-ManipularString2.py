nome = "emerson"
idade = 26
trabalho = "trabalha na mercedez"

print(nome + " tem " + str(idade) + " anos de idade e " + trabalho)
#utilizei a conversão acima pois no python não concatena numero com string diretamente,então tive que converter o numero para uma string.  

print("{} tem {} anos de idade e {}".format(nome,idade,trabalho))#aqui utilizei o metodo format que é mais simples e eficiente do que a conversão,pode ser considerado uma boa prática.
#basicamente é usar aspas simples ou duplas e no local que deseja colocar os valores correspondentes utilizar as chaves "{}" e no final das aspas por o ponto format com parenteses e os valores em ordem que desejar combinando com o que deseja: .format(valor1,valor2,valor3)
print(f'{nome} tem {idade} anos de idade e {trabalho}')#esse metodo é ainda mais implkes e rápido do que o format(sempre dá pra melhorar rsrs),basicamente utilizamos o f como gatilho principal e depois aspas simples ou duplas(sua escolha),abrimos e fechamos chaves {"coloque o valor aqui"} e só partir para o abraço.


