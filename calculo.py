#calcular o valor de uma compra.
def calcular_compra(valor_unitario, numero_itens):
    return valor_unitario * numero_itens

valor_unitario= int(input("Digite o valor unitário do produto:"))
quantidade_itens= int(input("Digite a quantidade do produto:"))
valor_total= calcular_compra(valor_unitario,quantidade_itens)
print(f"O valor do Total da Compra é R$ {valor_total:.2f}")