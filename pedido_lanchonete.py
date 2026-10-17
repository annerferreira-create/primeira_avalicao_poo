## Integrantes do grupo:
# - Anne Regina 
# - Dinara Dutra 

nome = "Felipe"
produto = "Hambúrguer"
quantidade = 3
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