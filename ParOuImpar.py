from random import randint
print("-=" * 15)
print("Vamos jogar PAR ou ÍMPAR?")
print("-=" * 15)
vitorias = 0
while True:
    v = int(input("Digite um valor: "))
    pc = randint(0, 10)
    pi = ' '
    soma = pc + v
    while pi not in "PI":
        pi = str(input("PAR ou ÍMPAR [P/I]? ")).strip().upper()[0]
    print(f"Você jogou {v} e o computador jogou {pc}. Total de {soma}, ", end='')
    print(f"deu par." if soma % 2 == 0 else "deu ímpar.")
    if pi == "P":
        if soma % 2 == 0:
            print("-" * 25)
            print("Você venceu!!!")
            print("-" * 25)
            vitorias += 1
        else:
            print("-" * 25)
            print("Você perdeu!!!")
            break
    elif pi == "I":
        if soma % 2 != 0:
            print("-" * 25)
            print("Você venceu!!!")
            print("-" * 25)
            vitorias += 1
        else:
            print("-" * 25)
            print("Você perdeu!!!")
            break
    print("Vamos tentar novamente...")
print(f"GAME OVER. Você venceu {vitorias} vez(es).")
