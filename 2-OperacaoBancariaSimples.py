#OPERAÇÃO BANCARIA SIMPLES 
saldoconta = 0

Deposito = input("Valor a ser depositado: ")
Deposito = float(Deposito)
saldoposDeposito = Deposito + saldoconta
saldoposDeposito = float(saldoposDeposito)

Saque = input("Digite quanto deseja resgatar: ")
Saque = float(Saque)
valorposSaque = saldoposDeposito - Saque
valorposSaque = float(valorposSaque)


ExtratoConta = input("Deseja exibir saldo da conta?(Sim ou Nao)")
        

if(Saque > Deposito):
    print("Valor de saque maior do que saldo total da conta!")

elif(Deposito >= Saque):
    print("Valor de saque de: R$", Saque,  "Realizado com sucesso!")
    

else:
    print("Não há valores disponiveis!")
    
   


match ExtratoConta:
    case "Sim":
        Saldo = Deposito - Saque
        print("Saldo da conta: R$ ","%.2f" % Saldo)
    
    case "Nao":
        print("Operação será encerrada em 3 Segundos: 3...2...1...Operacao finalizada!")    
 
    

    
