import csv

def ler_arquivo_cliente(nome_arquivo):
    clientes = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as file:
        leitor = csv.reader(file, delimiter=';')
        for linha in leitor:
            if len(linha) < 4:  # Ignorar linhas mal formatadas ou vazias
                continue
            cliente = {
                'nome': linha[0],
                'cidade': linha[1],
                'idade': int(linha[2]),
                'renda': float(linha[3])
            }
            clientes.append(cliente)
    return clientes
