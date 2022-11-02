class Julkaisu:
    def __init__(self, nimi):
        self.nimi=nimi
        
    def tulosta_tiedot(self):
        print(self.nimi)

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super(Kirja, self).__init__(nimi)

    def tulosta_tiedot(self):
        super(Kirja, self).tulosta_tiedot()
        print(f'Kirjan kirjoittaja on: {self.kirjoittaja} ja sivuja siinä on yhteensä: {self.sivumaara}.')


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super(Lehti, self).__init__(nimi)

    def tulosta_tiedot(self):
        super(Lehti, self).tulosta_tiedot()
        print(f'Lehden päätoimittaja on: {self.paatoimittaja}.')


julkaisut= []

julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))


for huisinhauskahuippujuttu in julkaisut:
    huisinhauskahuippujuttu.tulosta_tiedot()