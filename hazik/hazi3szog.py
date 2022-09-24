def haromszog(name,name2,name3):
    helyes = "A {},{} és {} oldalú háromszög szerkeszthető."
    helytelen = "A {},{} és {} oldalú háromszög NEM szerkeszthető."
    if a+b>=c and a+c>=b and b+c>=a:
        print(helyes.format(a,b,c))
    else:
        print(helytelen.format(a,b,c))

if __name__ == "__main__":
    print("Adja meg a háromszög három oldalát cm-ben:")
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))
    haromszog(a,b,c)
