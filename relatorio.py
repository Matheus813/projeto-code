from functools import reduce

def acima_do_minimo(venda):
    """diz se a venda entra no relatorio."""
    return venda["valor"] > VALOR_MINIMO

def aplicar_imposto(venda):
    """devolve uma nova venda com o valor liquido.

    nao altera a venda recebida. essa e a diferenca entre uma funcao pura e uma que modifica no lugar.
    """
    return {**venda, "valor": venda["valor"] * (1 - IMPOSTO)}

def agrupar_por_categoria(acumulado, venda):
    """Soma a venda no total da sua categoria."""
    cat = venda["categoria"]
    return {**acumulado, cat: acumulado.get(cat, 0) + venda["valor"]}

VENDAS = [
    {"produto": "teclado", "valor": 150.00, "categoria": "periferico"},
    {"produto": "mouse", "valor": 80.00, "categoria": "periferico"},
    {"produto": "monitor", "valor": 900.00, "categoria": "tela"},
    {"produto": "cabo HDMI", "valor": 35.00, "categoria": "acessorio"},
    {"produto": "headset", "valor": 250.00, "categoria": "periferico"},
    {"produto": "suporte", "valor": 120.00, "categoria": "acessorio"},

]

IMPOSTO = 0.10
VALOR_MINIMO = 100.00

def relatorio(venda):
    """Total liquido por categoria, apenas de venda acima do minimo."""
    relevantes = filter(acima_do_minimo, venda)
    liquidas = map(aplicar_imposto, relevantes)
    return reduce(agrupar_por_categoria, liquidas, {})

    for v in venda:
        if not acima_do_minimo(v):
            continue

        liquido = v["valor"] * (1 - IMPOSTO)
        cat = v["categoria"]

        if cat not in total_por_categoria:
            total_por_categoria[cat] = 0
        total_por_categoria[cat] += liquido

    return total_por_categoria

if __name__ == "__main__":
    for categoria, total in relatorio(VENDAS).items():
        print (f"{categoria:12} R$ {total:8.2f}")