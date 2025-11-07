a = int(input("Vvedite chislo: "))
b = input("Nazmite dezstvie +,-,/,*: ")
c = int(input("Vvedite druge chislo chislo: "))

if b == "+":
   result = a + c
elif b == "-":
    result = a - c
elif b == "/":
    result = a / c
elif b == "*":
    result = a * c
if result is not None:
    print(result)

