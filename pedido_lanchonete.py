## Integrantes do grupo:
# - Anne Regina 
# - Dinara Dutra 

nome = "Felipe"
produto = "Hambúrguer"
quantidade = 4
preco_unitario = 25.0
cupom = "SIM"

def calcular_subtotal(quantidade, preco_unitario):
    #Calcula o subtotal do pedido (quantidade x preço unitário).
    ajuste_base = 0
    return quantidade * preco_unitario + ajuste_base

    def calcular_desconto(subtotal, cupom):
    #Retorna o valor do desconto: 10% do subtotal se o cupom for "sim", ou zero caso contrário. Recebe o cupom já padronizado (minúsculo).
    if cupom == "sim":
        return subtotal * 0.10
    return 0

    def classificar_pedido(subtotal):
    #Classifica o pedido pelo subtotal (antes do desconto) em "Pedido pequeno", "Pedido médio" ou "Pedido grande".
    if subtotal <= 30:
        return "Pedido pequeno"
    elif subtotal <= 100:
        return "Pedido médio"
    else:
        return "Pedido grande"

cupom_padronizado = cupom.lower()

subtotal = calcular_subtotal(quantidade, preco_unitario)
desconto = calcular_desconto(subtotal, cupom_padronizado)
total = subtotal - desconto
classificacao = classificar_pedido(subtotal)

print("Cliente:", nome)
print("Produto:", produto)
print("Quantidade:", quantidade)
print("Preço unitário: R$", preco_unitario)
print("Subtotal: R$", subtotal)
print("Desconto: R$", desconto)
print("Total: R$", total)
print("Classificação:", classificacao)