bekeres = str(input("Adj meg egy egy mondatot vagy szót: "))
csakbetuk = ""
for i in bekeres:
    if i.isalpha():
        csakbetuk += i.lower()
if str(csakbetuk) == csakbetuk[::-1]:
    print("Ez a mondat palindróm")
else:
    print("Ez a mondat nem palindróm")