codigos_produtos = [int(input("Digite o código do produto: ")) for _ in range(10)]
estoque_produtos = [int(input("Digite a quantidade em estoque do produto: ")) for _ in range(10)]

def verificar_codigo(codigo, codigos):
    if codigo in codigos:
        return True, codigos.index(codigo)
    else:
        return False, -1
while True:
    codigo_cliente = int(input("Digite o código do cliente (0 para sair): "))
    if codigo_cliente == 0:
        break
    codigo_produto = int(input("Digite o código do produto desejado: "))
    quantidade_desejada = int(input("Digite a quantidade desejada: "))
    existe_codigo, indice = verificar_codigo(codigo_produto, codigos_produtos)
    if not existe_codigo:
        print("Código inexistente.")
        continue
    print("Código existente.")
    if estoque_produtos[indice] >= quantidade_desejada:
        print("Nova remessa atendida integralmente.")
        estoque_produtos[indice] -= quantidade_desejada
    elif estoque_produtos[indice] > 0:
        print("Pedido atendido parcialmente.")
        estoque_produtos[indice] = 0
    else:
        print("Não temos estoque suficiente.")
print("Estoque atualizado:")
for codigo, estoque in zip(codigos_produtos, estoque_produtos):
    print(f"Código do produto: {codigo}, Estoque: {estoque}")

