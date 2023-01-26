def elso_idos(lista):
    i = 0
    nincsmeg = True
    index = 0
    while i < len(lista) and nincsmeg:
        if i > 70:
            nincsmeg = False
            index = i
        i += 1
    return index


def konzolra_ir(idos):
    print(f"\nII/D, E:\n\tElső idős ember korának helye a listában:{idos}")


def fajl_ir(idos):
    ki = open("oreg.txt", "w", encoding="utf8")
    print(f"II/F:\n\tElső idős ember korának helye a listában:{idos}", file=ki)
    ki.close()


def feladat2():
    lista = []
    i = 0
    while i < 5:
        kor = int(input("Adj meg egy éltkort [0-120]:"))
        lista.append(kor)
        i += 1

    print(f"II/A, B, C:\n\t{lista[0]}", end="")
    i = 1
    while i < len(lista):
        print(f" : {lista[i]}", end="")
        i += 1

    idos = elso_idos(lista)
    konzolra_ir(idos)
    fajl_ir(idos)
