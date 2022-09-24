def cm_to_inch(name,name2):
    valt = 2.54
    cmvalt = round(szam*valt,2)
    inchvalt = round(szam/valt,2)
    if mert == "inch":
        print(inchvalt,"cms")
    elif mert == "cm":
        print(cmvalt,"inches")
    else:
        print("Not correct unit!")

if __name__ == "__main__":
    print("Adjon meg egy számot és egy mértékegységet: ")
    szam = int(input(""))
    mert = input("")
    cm_to_inch(szam,mert)
    