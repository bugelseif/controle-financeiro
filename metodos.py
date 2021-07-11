# from controle_financeiro import movimentos
from datetime import MINYEAR, date, datetime
import dateutil.relativedelta


def imprimirMovimentacoes(movimentacao, exibicao):
    """arg: movimentacao = uma movimentacao na conta
       arg: exibicao = verdadeiro indica exibição completa, falso infica exibição resumida
    """
    if (exibicao):
        print(f"Movimentação de {movimentacao['valor']} em {movimentacao['data']} com o motivo de {movimentacao['motivo']}, observações de {movimentacao['observacoes']}, inserido por {movimentacao['inseridoPor']} e de responsabilidade de {movimentacao['responsavel']}")
    else: 
        print(f"Movimentação de {movimentacao['valor']} em {movimentacao['data']}")


def exibirSaldoTotal(movimentos):
    """arg: movimentos = array com dicionarios."""
    total = 0
    for i in movimentos:
        total += i['valor']
    print(f'O saldo total é {total}')


def exibirEntradas(movimentos, meses = 1):
    """arg: movimentos = array com dicionarios,
       arg: meses = quantos meses anteriores à data atual serão considerados."""
    now = date.today()
    meses_considerados = now + dateutil.relativedelta.relativedelta(months=-meses)
    print("""indique o tipo de visualização
        (1) resumido (padrão) | (2) completo
        """)
    visualizacao = int(input())
    for i in movimentos:
        if i['valor'] > 0 and meses_considerados <= now: 
            imprimirMovimentacoes(i, visualizacao == 2)




def exibirSaidas(movimentos, meses = 1):
    """arg: movimentos = array com dicionarios,
       arg: meses = quantos meses anterior a data atual."""
    now = date.today()
    menos = now + dateutil.relativedelta.relativedelta(months=-meses)

    print("""indique o tipo de visualização
        (1) resumido (padrão) | (2) completo
        """)
    visualizacao = int(input())

    for i in movimentos:
        if i['valor'] < 0 and menos < now:
            imprimirMovimentacoes(i, visualizacao == 2)

def exibirExtrato(movimentos):
    """arg: movimentos = array com dicionarios."""
    now = date.today()
    print('''indique o periodo
    (1) 7 dias | (2) 15 dias  | (3) 6 meses  | (4) total (padrão)
    ''')
    periodo = int(input())
    
    menos = now

    if (periodo == 1):
        menos = now + dateutil.relativedelta.relativedelta(days=-7)
    elif (periodo ==2):
        menos = now + dateutil.relativedelta.relativedelta(days=-15)
    elif (periodo ==3):
        menos = now + dateutil.relativedelta.relativedelta(months=-6)
    else:
        menos = date(1990,1,1)

    print("""indique o tipo de visualização
        (1) resumido (padrão) | (2) completo
    """)

    visualizacao = int(input())

    for i in movimentos:
        print("oi")
       ##Implementar
        if menos <= date.now():#datetime.strptime(i['data'],'%Y-%m-%d').date():
            imprimirMovimentacoes(i, visualizacao == 2)

            print("o")
            # print(f'Movimentação {} em {} ')
            # if i['valor'] > 0:
            #     print('entradas')
            #     print(i['data'])
            #     print(i['valor'])
            # else:
            #     print('saidas')
            #     print(i['data'])
            #     print(i['valor'])

    #verificar erros na comparação de data e melhorar saidas

def novoLancamento(movimentos):
    """arg: movimentos = array com dicionarios."""
    id = 8 #autoincremento
    valor = float(input('Digite o valor '))
    motivo = input('Digite o motivo ')
    data = input('Digite a data aaaa-mm-dd ')
    responsavel = input('Digite o nome do responsavel ')
    observacoes = input('Observações: ')
    inseridoPor = input('Digite seu nome')
    novo = {"id": id, "valor":valor, "motivo":motivo, "data": data,"Responsavel": responsavel, "Observacoes": observacoes, "InseridoPor": inseridoPor}

    movimentos.append(novo)


def editarLancamento(movimentos, id):
    """arg: movimentos = array com dicionarios.
       arg: # id = identifica qual modificar."""
    for i in movimentos:
        if i['id'] == id:
            print(f"Editar id:{i['id']}")
            i['motivo'] = input('Digite o motivo ')
            i['data'] = input('Digite a data aaaa-mm-dd ')
            i['responsavel'] = input('Digite o nome do responsavel ')
            i['observacoes'] = input('Observações: ')
            i['inseridoPor'] = input('Digite seu nome ')


