
def GerenciamentoComprasProdutos():
    dados_compras = {}
    while True:
        produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
        if produto.lower() == 'sair':
            break
        quantidade = int(input("Digite a quantidade comprada: "))
        preco = float(input("Digite o preço unitário: "))
        usuario = input("Digite o nome do usuário: ")
        soma = quantidade * preco
        dados_compras[produto] = {'quantidade': quantidade, 'preco': preco, 'usuario': usuario, 'Total Gasto': soma}
    return dados_compras
print(GerenciamentoComprasProdutos())