n = int(input("Podaj n"))
a = 1
suma = 0

while a<=n:
    b=int(input(f"Podaj liczbę punktów studenta {a} :"))
    if (b<0 or b>100):
        continue
    suma+=b
    a+=1

print(suma/n)