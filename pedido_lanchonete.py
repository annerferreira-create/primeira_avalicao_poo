# Integrantes do grupo:
# - Anne Regina
# - Dinara Dutra

nome = "Felipe"
produto = "Hambúrguer"
quantidade = 3
preco_unitario = 25.0
cupom = "SIM"

def calcular_subtotal(quantidade, preco_unitario):
    """Calcula e retorna o subtotal do pedido multiplicando quantidade e preço unitário."""
    return quantidade * preco_unitario

def calcular_desconto(subtotal, cupom):
    """Recebe o cupom padronizado e retorna o valor numérico do desconto (10% se 'sim')."""
    if cupom == "sim":
        return subtotal * 0.10
    return 0

def classificar_pedido(subtotal):
    """Classifica o pedido em pequeno, médio ou grande com base no subtotal."""
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
