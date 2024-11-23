#calcular o valor de uma compra.
def calcular_compra(valor_unitario, numero_itens):
    return valor_unitario * numero_itens

def aplicar_desconto(total_compra, desconto):
    desconto = total_compra *(desconto/100)
    return total_compra - desconto

valor_unitario= int(input("Digite o valor unitário do produto:"))
quantidade_itens= int(input("Digite a quantidade do produto:"))

valor_total= calcular_compra(valor_unitario,quantidade_itens)
d= int(input("Informe o desconto a ser aplicado:"))

total_com_desconto= aplicar_desconto (valor_total,d)

print(f"O valor do Total da Compra é R$ {total_com_desconto:.2f}")
