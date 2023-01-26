import random


def feladat1():
    szam = random.randint(1, 50)
    print(f"I/A:\n\tA generált szám: {szam}")
    print(f"I/B")
    if szam % 15 == 0:
        print("\tA szám öttel és hárommal is osztható!")
    elif szam % 5 == 0:
        print("\tA szám öttel osztható!")
    elif szam % 3 == 0:
        print("\tA szám hárommal osztható!")
