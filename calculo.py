#calcular o valor de uma compra.
def calcular_compra(valor_unitario, numero_itens):
    return valor_unitario * numero_itens

v_u= float(input("Digite o valor unitário do produto:"))
q_i= int(input("Digite a quantidade do produto:"))
valor_total= calcular_compra(v_u,q_i)
print(f"O valor do Total da Compra è R$ {valor_total:.2f}")