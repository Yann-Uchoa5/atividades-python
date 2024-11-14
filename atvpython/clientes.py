import util

def calcular_media_idade(clientes):
    total_idade = sum(cliente['idade'] for cliente in clientes)
    return total_idade / len(clientes) if clientes else 0

def calcular_media_renda(clientes):
    total_renda = sum(cliente['renda'] for cliente in clientes)
    return total_renda / len(clientes) if clientes else 0

def main():
    nome_arquivo = 'clientes.txt'
    clientes = util.ler_arquivo_cliente(nome_arquivo)

    media_idade = calcular_media_idade(clientes)
    media_renda = calcular_media_renda(clientes)

    print(f'Média de Idade: {media_idade:.2f}')
    print(f'Média de Renda Mensal: R${media_renda:.2f}')

if __name__ == '__main__':
    main()
