sayilar = []
while True:
    x = input("Sayıyı giriniz: ")
    if x == ("q"):
        break
    else:
        sayilar.append(int(x))


cift = 0
tek = 0
for i in sayilar:
    if i % 2 == 0:
        cift += i
    else:
        tek += i


if tek == 0:
    print("Tanımsız")
else:
    sonuc = cift / tek
    print(sonuc)

