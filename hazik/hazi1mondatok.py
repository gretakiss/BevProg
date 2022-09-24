def mondatbetuk(name):
    betuk = {}
    for x in name:
        if x in betuk:
            betuk[x] += 1
        else:
            betuk[x] = 1
    print("Betűk gyakorisága:", betuk)
    print("Fordítva:", mondat[-1::-1])
    szavak = mondat.split(" ")
    print("Listába rendezve szavanként:", szavak)

if __name__ == "__main__":
    mondat = input("Adjon meg egy mondatot:")

    mondatbetuk(mondat)

