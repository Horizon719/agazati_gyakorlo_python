class Gosztaly:

    def __init__(self, sor):
        adatok = sor.split("@")
        self.neve = adatok[0]
        self.nemzettseg = adatok[1]
        self.evszak = adatok[2]
