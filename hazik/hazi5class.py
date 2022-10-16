class Team:
    def __init__(self,nev,projekt,szerepkor):
        self.nev = nev
        self.projekt = projekt
        self.szerepkor = szerepkor
        print("-- Developer létrehozva. --")
        print("{} a {}-en dolgozik {} szerepkörben.".format(self.nev, self.projekt, self.szerepkor))
        
    def __eq__(self, masik_tag):
        return self.projekt == masik_tag.projekt and self.nev != masik_tag.nev
def sameprojekt():
    tagok = [tag1, tag2, tag3, tag4]
    for tag in tagok:
        for masik_tag in tagok:
            if tag == masik_tag:
                print("{} és {} dolgoznak egy projekten.".format(tag.nev, masik_tag.nev))
        tagok.remove(tag)

if __name__ =="__main__":
    tag1 = Team("Ricsi", "SolArch", "Frontend")
    tag2 = Team("Angéla", "ZerTeng", "Tesztelő")
    tag3 = Team("Peti", "KefERP", "Backend")
    tag4 = Team("Éva", "KefERP", "Frontend")
    print()
    sameprojekt()



