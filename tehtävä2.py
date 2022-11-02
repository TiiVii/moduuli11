import random

class auto():
    def __init__(self, rekisteri, hnopeus, thnopeus):
        self.rekisteri = rekisteri
        self.hnopeus = hnopeus
        self.thnopeus = random.randint(0,self.hnopeus)
        self.matka = 0

    def tulosta_tiedot(self):
        print(f'Auton rekisteri on: {self.rekisteri} ja sen huippunopeus on: {self.hnopeus} km/h.')

    def kulje(self, tunnit):
        self.tunnit = 0
        self.matka += tunnit * self.thnopeus

class Sahko(auto):
    def __init__(self, rekisteri, hnopeus, akkukapasiteetti, thnopeus):
        self.akkukapasiteetti=akkukapasiteetti
        super(Sahko, self).__init__(rekisteri, hnopeus, thnopeus)

    def tulosta_tiedot(self):
        super(Sahko, self).tulosta_tiedot()
        print(f'Auton akkukapasiteetti on {self.akkukapasiteetti} kWh. Kuljettu matka on yhteensä: {self.matka} km.')


class Polttomoottori(auto):
    def __init__(self, rekisteri, hnopeus, bensatankinkoko, thnopeus):
        self.bensatankinkoko=bensatankinkoko
        super(Polttomoottori, self).__init__(rekisteri, hnopeus, thnopeus)

    def tulosta_tiedot(self):
        super(Polttomoottori, self).tulosta_tiedot()
        print(f'Auton bensatankin koko on: {self.bensatankinkoko} l. Kuljettu matka on yhteensä: {self.matka} km.')


sauto= Sahko("ABC-15", 180, 52.5, 160)
pauto= Polttomoottori("ACD-123", 165, 32.3, 111)

sauto.kulje(3)
pauto.kulje(3)

sauto.tulosta_tiedot()
pauto.tulosta_tiedot()
