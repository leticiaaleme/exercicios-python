contador = 0
while True:
    v = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 25)
    if v < 0:
        break
    for contador in range(0, 10):
        contador += 1
        vezes = v * contador
        print(f"{v} x {contador:2} = {vezes:3}")
    print("-" * 25)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
