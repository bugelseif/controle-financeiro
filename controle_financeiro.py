from dados import movimentos
from metodos import *

while (True):
    print(""" Selecione a opção
    0) Sair da aplicação
    1) Ver saldo total
    2) Ver entradas na conta
    3) Ver saídas da conta
    4) Ver extrato
    5) Adicionar nova movimentação
    6) Editar aplicação existente""")

    opcao = int(input())
    if opcao == 0:
        break
    elif opcao == 1:
        exibirSaldoTotal(movimentos)
    elif opcao == 2:
        exibirEntradas(movimentos, 10)
    elif opcao == 3:
        exibirSaidas(movimentos, 10)
    elif opcao == 4:
        exibirExtrato(movimentos)
    elif opcao == 5:
        novoLancamento(movimentos)
    elif opcao == 6:
        identificador = int(input("Qual o id da movimentação que deseja modificar? (digite -1 para cancelar)"))
        editarLancamento(movimentos, identificador)
    else:
        print("Opção inválida. Tente novamente.")
    
    # input("Aperte enter para continuar")
    # limpar a tela

#Finalização da aplicação
print("Saindo da aplicação")
