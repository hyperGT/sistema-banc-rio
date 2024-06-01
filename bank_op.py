import random

valor_conta = random.randint(0, 5000)
limite=3

# funções
def menu() -> int:
    print("""
          -----Menu-----
          
          [0] sair
          [1] Saque
          [2] Depósito
          [3] Exibir Extrato
          
          \n\n""");
    resp = int(input("Insira o número correspondente a operação que deseja realizar: "))
    return resp

def sacar(saque: int, limite: int) -> int:
    if(valor_conta <=0 ):
        print("Não é possível sacar, o saldo é inexistente ou negativo.")
        return 0, limite
    elif(limite > 0):
        while True:
            saque = int(input("Insira valor para saque até R$500: "))
            
            if(saque<=500):
                return saque, limite - 1
            else:
                print("Valor inválido, Insira um valor de até 500 reais")
                return 0, limite
    else:
        print("Limite diário atingido")
    
def deposito(val_atual: int, depositos: list) -> int:
    
    depositar = int(input("Insira o valor do depósito: "))    
    
    depositos.append(depositar)
    
    return val_atual+depositar

def extrato(saques: list, depositos: list, saldo: int) -> None:
    print(f"""
      -------------Extrato-------------
      Valores dos saques realizados: {saques}
      Valores dos depósitos realizados: {depositos}
      Saldo atual da conta: R${saldo}
      """)

print(f"""
          Limite diário de saque: {limite}
          Saldo atual da conta: R${valor_conta}
          """)

# declarando duas listas, cada uma guarda informações a respeito dos valores
lista_saques = []
depositos = []


while True:    
    
    operacao = menu()
    
    if(operacao == 1):
              
        saque, limite = sacar(saque, limite)  # atualizando a variavel saque
        lista_saques.append(saque) # atualizando a lista dos valores dos saques feitos
        valor_conta -= saque # descontando o valor do saque no saldo da conta
    elif(operacao == 2):
        valor_conta = deposito(valor_conta, depositos)
    elif(operacao == 3):
        extrato(lista_saques, depositos, valor_conta)
    else:
        break
