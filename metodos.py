# from controle_financeiro import movimentos
from datetime import MINYEAR, date, datetime
import dateutil.relativedelta


def imprimirMovimentacoes(movimentacao, tipoMovimentacao, exibicao):
    """arg: movimentacao = uma movimentacao na conta
       arg: exibicao = verdadeiro indica exibição completa, falso infica exibição resumida
    """
    if (exibicao):
        print(f"{tipoMovimentacao} (id: {movimentacao['id']}) de {abs(movimentacao['valor'])} em {movimentacao['data']} com o motivo de {movimentacao['motivo']}, observações de {movimentacao['observacoes']}, inserido por {movimentacao['inseridoPor']} e de responsabilidade de {movimentacao['responsavel']}")
    else: 
        print(f"{tipoMovimentacao} (id: {movimentacao['id']}) de {abs(movimentacao['valor'])} em {movimentacao['data']}")


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
            imprimirMovimentacoes(i, "Entrada", visualizacao == 2)


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
            imprimirMovimentacoes(i, "Saída", visualizacao == 2)

def exibirExtrato(movimentos):
    """arg: movimentos = array com dicionarios."""
    now = date.today()
    print('''indique o periodo
    (1) 7 dias | (2) 15 dias  | (3) 6 meses  | (4) total (padrão)
    ''')
    periodo = int(input())
    
    tempo_considerado = now

    if (periodo == 1):
        tempo_considerado = now + dateutil.relativedelta.relativedelta(days=-7)
    elif (periodo ==2):
        tempo_considerado = now + dateutil.relativedelta.relativedelta(days=-15)
    elif (periodo ==3):
        tempo_considerado = now + dateutil.relativedelta.relativedelta(months=-6)
    else:
        tempo_considerado = date(1990,1,1)

    print("""indique o tipo de visualização
        (1) resumido (padrão) | (2) completo
    """)

    visualizacao = int(input())

    for i in movimentos:
        #Modificar a condição do if
        #if menos <= date.datetime.strptime(i['data'],'%Y-%m-%d').date():
        if True:
            if i['valor'] > 0:
                imprimirMovimentacoes(i, "Entrada", visualizacao ==2)
            else:
                imprimirMovimentacoes(i, "Saída", visualizacao ==2)


def novoLancamento(movimentos):
    """arg: movimentos = array com dicionarios."""
    id = len(movimentos) + 1
    print("""Indique a movimentação
        (1) Entrada na conta (padrão) | (2) Saída da conta
    """)  
    operacao = int(input())

    valorLido = float(input('Digite o valor movimentado: '))
    valorParaSalvar = 0 - valorLido if operacao == 2 else valorLido # modifica o valor pra ser salvo se for uma entrada ou saída
    
    motivo = input('Digite o motivo: ')
    data = date.today()
    responsavel = input('Digite o nome da responsavel: ')
    observacoes = input('Observações (digite - se não houverem observações): ')
    inseridoPor = input('Digite seu nome: ')
    
    novo = {"id": id, "valor":valorParaSalvar, "motivo":motivo, "data": data,"responsavel": responsavel, "observacoes": observacoes, "inseridoPor": inseridoPor}
    print("Digite s para salvar a movimentação, caso contrário digite n")
    salvar = input()
    if(salvar.lower() == 's'):
        movimentos.append(novo)

def ativarModificacaoCampo(texto):
    """arg: texto = texto a ser impresso antes do pedido de confirmação""""
    print(texto)
    print("Digite s para modificar, caso contrário digite n")
    continuar = input()
    if(continuar.lower() == 's'):
        return True
    return False

def editarLancamento(movimentos, identificador):
    """arg: movimentos = array com dicionarios.
       arg: # id = identifica qual modificar."""
    for i in movimentos:
        if i['id'] == identificador:
            print(f"Editar movimentação: ")
            if i['valor'] > 0:
                imprimirMovimentacoes(i, "Entrada", True)
            else:
                imprimirMovimentacoes(i, "Saída", True)
            #informações obrigatórias
            i['data'] = date.today()
            i['inseridoPor'] = input('Digite seu nome: ')
            #informações optativas
            if(ativarModificacaoCampo("Deseja alterar o motivo?")):
                 i['motivo'] = "MODIFICADO: " + input('Digite o novo motivo: ')
            if(ativarModificacaoCampo("Deseja alterar a responsável?")):
                 i['responsavel'] = "MODIFICADO: " + input('Digite o nome da nova responsavel ')
            if(ativarModificacaoCampo("Deseja alterar as observações?")):
                 i['observacoes'] = "MODIFICADO: " + input('Observações(digite - se não houverem observações): ')

