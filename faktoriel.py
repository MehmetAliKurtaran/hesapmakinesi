x = int(input("Sayı gir: "))
y = 1
for i in range(1,x+1):
    y *= i
print(f"{x}! =",y)