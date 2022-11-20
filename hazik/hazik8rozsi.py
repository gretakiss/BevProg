import string
def novella ():
    sorok = ""
    rmirasjel = ""
    with open("hazi.txt","r",encoding="UTF-8") as f:
        sor = f.readline()
        while sor:
            if sor != "\n":
                sorok += sor
            sor = f.readline()
        for i in sorok:
            if i != " " and i not in string.punctuation:
                rmirasjel += i

        maganh = "aáeéiíöőoóüűúuAÁIÍOÓÖŐÜŰÚUEÉ"
        rmmaganh = ""
        for i in rmirasjel:
            if i not in maganh:
                rmmaganh += i


    kifele = list(rmmaganh.split("\n"))
    with open("kimenet.txt","w",encoding="UTF-8") as k:
        for srszam,line in enumerate(kifele):
            if (srszam+1) % 3 == 0:
                k.write(line + "\n")

if __name__ == "__main__":
    novella()
