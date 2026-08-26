valor = 20.01

cupom = input("você tem cupom? (s/n) ").lower()

if cupom == "s" or valor > 300:
    print("frete $R0,00")
    print(f"{valor:.2f}")

elif valor >= 100 and valor <= 300:
    print("frete de $R8,00")
    print(f"{valor:.2f}")
else:
    print("frete de $R15,00")
    print(f"{valor:.2f}")

