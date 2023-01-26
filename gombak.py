import Gosztaly


def feladat3():
    def gombak_szama():
        print(f"III/A, B:\n\tA gombák száma:{len(lista)}")

    def papsapka():
        index = 0
        nincsmeg = True
        while index < len(lista) and nincsmeg:
            if lista[index].nemzettseg == "papsapkagombák ":
                print(f"III/C:\n\tAz első papsapkagomba neve: {lista[index].neve}")
                nincsmeg = False
            index += 1

    def tinoru():
        index = 0
        db = 0
        while index < len(lista):
            if lista[index].nemzettseg == "tinóru":
                db += 1
            index += 1
        print(f"III/D:\n\t	A tinóru gombák száma: {db}")

    lista = []
    i = 0
    be = open("gombak.txt", "r", encoding="utf8")
    sorok = be.readlines()
    while i < len(sorok):
        adatok = sorok[i]
        tiszta = adatok.strip()
        sor = Gosztaly.Gosztaly(tiszta)
        lista.append(sor)
        i += 1
    be.close()

    gombak_szama()
    papsapka()
    tinoru()
