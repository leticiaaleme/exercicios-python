import random
import time
print("""Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
lista = ["Pedra", "Papel", "Tesoura"]
pc = random.choice(lista)
escolha = int(input("Qual é a sua jogada? "))
time.sleep(1)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")
time.sleep(1)
print("-=" * 20)
if escolha == 1:
    if pc == lista[0]:
        print("Jogador escolheu Pedra.")
        print("Computador jogou {}.".format(pc))
        print("-=" * 20)
        print("\033[31mEMPATE!!!\033[m")
    elif pc == lista[1]:
        print("Jogador escolheu Pedra.")
        print("Computador jogou {}.".format(pc))
        print("-=" * 20)
        print("\033[32mCOMPUTADOR VENCE!!!\033[m")
    elif pc == lista[2]:
        print("Jogador escolheu Pedra.")
        print("Computador jogou {}.".format(pc))
        print("-=" * 20)
        print("\033[34mJOGADOR VENCE!!!\033[m")
elif escolha == 2:
    if pc == lista[1]:
        print("Jogador escolheu Papel.")
        print("Computador jogou {}.".format(pc))
        print("-=" * 20)
        print("\033[31mEMPATE!!!\033[m")
    elif pc == lista[0]:
        print("Jogador escolheu Papel.")
        print("Computador jogou {}.".format(pc))
        print("-=" * 20)
        print("\033[34mJOGADOR VENCE!!!\033[m")
    elif pc == lista[2]:
        print("Jogador escolheu Papel.")
        print("Computador jogou {}.".format(pc))
        print("-=" * 20)
        print("\033[32mCOMPUTADOR VENCE!!!\033[m")
elif escolha == 3:
    if pc == lista[2]:
        print("Jogador escolheu Tesoura.")
        print("Computador jogou {}.".format(pc))
        print("-=" * 20)
        print("\033[31mEMPATE!!!\033[m")
    elif pc == lista[0]:
        print("Jogador escolheu Tesoura.")
        print("Computador jogou {}.".format(pc))
        print("-=" * 20)
        print("\033[32mCOMPUTADOR VENCE!!!\033[m")
    elif pc == lista[1]:
        print("Jogador escolheu Tesoura.")
        print("Computador jogou {}.".format(pc))
        print("-=" * 20)
        print("\033[34mJOGADOR VENCE!!!\033[m")
else:
    print("Jogada inválida.")
