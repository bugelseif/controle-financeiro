from controle_financeiro import movimentos
from datetime import MINYEAR, date, datetime
import dateutil.relativedelta

def exibirSaldoTotal(movimentos):
    """arg: movimentos = array com dicionarios."""

    total = 0
    for i in movimentos:
        total += i['valor']
    print(total)

def exibirEntradas(movimentos, meses):
    """arg: movimentos = array com dicionarios,
       arg: meses = quantos meses anteriores à data atual serão considerados."""
    now = date.today()
    menos = now + dateutil.relativedelta.relativedelta(months=-meses)

    for i in movimentos:
        if i['valor'] > 0 and menos < datetime.strptime(i['data'],'%Y-%m-%d').date():
            print(i['data'])
            print(i['valor'])


def exibirSaidas(movimentos, meses):
    """arg: movimentos = array com dicionarios,
       arg: meses = quantos meses anterior a data atual."""
    now = date.today()
    menos = now + dateutil.relativedelta.relativedelta(months=-meses)

    for i in movimentos:
        if i['valor'] < 0 and menos < datetime.strptime(i['data'],'%Y-%m-%d').date():
            print(i['data'])
            print(i['valor'])
            #verificar erro após o retorno dos valores

def exibirExtrato(movimentos):
    """arg: movimentos = array com dicionarios."""
    now = date.today()
    while True:
        print('''indique o periodo
        (1) 7 dias  | (2) 15 dias  | (3) 6 meses  | (4) total
          ''')
        periodo = int(input())
        if 0 < periodo < 5:
            print(f"periodo {periodo}")
            break
    if(periodo == 1):
        menos = now + dateutil.relativedelta.relativedelta(days=-7)
        for i in movimentos:
            if menos < datetime.strptime(i['data'],'%Y-%m-%d').date():
                if i['valor'] > 0:
                    print('entradas')
                    print(i['data'])
                    print(i['valor'])
                else:
                    print('saidas')
                    print(i['data'])
                    print(i['valor'])

    elif(periodo == 2):
        menos = now + dateutil.relativedelta.relativedelta(days=-15)
        for i in movimentos:
            if menos < datetime.strptime(i['data'],'%Y-%m-%d').date():
                if i['valor'] > 0:
                    print('entradas')
                    print(i['data'])
                    print(i['valor'])
                else:
                    print('saidas')
                    print(i['data'])
                    print(i['valor'])

    elif(periodo == 3):
        menos = now + dateutil.relativedelta.relativedelta(months=-6)
        for i in movimentos:
            if menos < datetime.strptime(i['data'],'%Y-%m-%d').date():
                if i['valor'] > 0:
                    print('entradas')
                    print(i['data'])
                    print(i['valor'])
                else:
                    print('saidas')
                    print(i['data'])
                    print(i['valor'])

    else:
        for i in movimentos:
            if i['valor'] > 0:
                print('entradas')
                print(i['data'])
                print(i['valor'])
            else:
                print('saidas')
                print(i['data'])
                print(i['valor'])
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


help(exibirSaldoTotal)