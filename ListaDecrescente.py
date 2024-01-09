lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    sn = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if sn in "N":
        break
print("-=" * 30)
print(f"Você digitou {len(lista)} valores.")
lista.sort(reverse=True)
print(f"Os números em ordem decrescente são {lista}")
if 5 in lista:
    print("O número 5 está na lista!")
else:
    print("O número 5 não está na lista...")
