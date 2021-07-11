from datetime import date
from metodos import *

movimentos =  [
    {"id": 1, "valor":1000, "motivo": "Venda de Bolinhos","data": date(2020, 12, 4).isoformat(),"responsavel": "lala","observacoes": "Deu muito dinheiro", "inseridoPor": "lala"},
    {"id": 2, "valor":-580.48, "motivo": "Ração de unicórnio","data": date(2020, 12, 5).isoformat(),"responsavel": "lala", "observacoes": "","inseridoPor": "lala"},
    {"id": 3, "valor":23.84, "motivo": "Patrocínio da shostners e shostners","data": date(2021, 1, 25).isoformat(),"responsavel": "lala", "observacoes": "Muita mão de vaquisse esse patrocínio","inseridoPor": "lolo"},
    {"id": 4, "valor":-1500, "motivo": "Compra de equipamentos","data": date(2021, 5, 10).isoformat(),"responsavel": "jaja", "observacoes": "", "inseridoPor": "lolo"},
    {"id": 5, "valor":1487.95, "motivo": "Ganhei na loteria","data": date(2021, 5, 24).isoformat(),"responsavel": "jaja", "observacoes": "Estamos ricos", "inseridoPor": "lala"},
    {"id": 6, "valor":-52.14, "motivo": "Compra de canetas","data": date(2021, 6, 7).isoformat(),"responsavel": "lala", "observacoes": "Nada a comentar", "inseridoPor": "lala"},
    {"id": 7, "valor":-714.41, "motivo": "coxinha pra todo mundo","data": date.today(),"responsavel": "lala", "observacoes": "Panças enchidas", "inseridoPor": "lala"}
]

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
        exibirEntradas(movimentos)
    elif opcao == 3:
        exibirSaidas(movimentos)
    elif opcao == 4:
        exibirExtrato(movimentos)
    elif opcao == 5:
        novoLancamento(movimentos)
    elif opcao == 6:
        identificador = int(input("Qual o id da movimentação que deseja modificar?"))
        editarLancamento(movimentos,identificador)
    else:
        print("Opção inválida. Tente novamente.")
    
    input("Aperte enter para continuar")
    ## limpar a tela

#Finalização da aplicação
print("Saindo da aplicação")
