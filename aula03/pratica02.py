preco = float(19.90)
quant = 3

print(int(preco))

total = preco - (preco / 10)

print(f"{total:.2f}")

print(preco, quant, preco * quant)

if preco > quant:
    print("preco maior que quant")

elif preco < quant:
    print("preco menor que quant")

else:
    print("preco igual a quant")