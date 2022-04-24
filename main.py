class Biblioteka:
    lista_ksiazek = []
    lista_egzemplarzy = []
    lista_krotek = []
    lista_ostateczna = []
    czy_jest_w_liscie = False
    def __init__(self, limit_wypozyczen):
        self.limit_wypozyczen = limit_wypozyczen

    def sortuj(self, e):
        return e['tytul']

    def dostepne_egzemplarze(self):
        for ksiazka in self.lista_ksiazek:
            for egzemplarze in self.lista_egzemplarzy:
                if egzemplarze.tytul == ksiazka.tytul and egzemplarze.autor == ksiazka.autor:
                    self.czy_jest_w_liscie = True
            if not self.czy_jest_w_liscie:
                self.lista_ostateczna.append({'tytul': ksiazka.tytul, 'autor': ksiazka.autor, 'ilosc_egzemplarzy': self.liczEgzemplarze(ksiazka)})
                self.czy_jest_w_liscie = False
                self.lista_egzemplarzy.append(ksiazka)
            self.czy_jest_w_liscie = False
        self.lista_ostateczna.sort(key=self.sortuj)
        for lista in self.lista_ostateczna:
            print("('" + lista['tytul'].strip() + "'" + "," + "'" + lista['autor'].strip() + "', " + lista['ilosc_egzemplarzy'].strip() + ")")

    def dodaj_egzemplarz_ksiazki(self, ksiazka):
        self.lista_ksiazek.append(ksiazka)

    def liczEgzemplarze(self, aktualna_ksiazka):
        wynik = 0
        for ksiazka in self.lista_ksiazek:
            if aktualna_ksiazka.tytul == ksiazka.tytul and aktualna_ksiazka.autor == ksiazka.autor:
                wynik += 1

        return str(wynik)

class Ksiazka:

    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

class Egzemplarz:

    def __init__(self, rok_wydania, wypozyczony):
        self.rok_wydania = rok_wydania
        self.wypozyczony = wypozyczony

class Czytelnik:

    def __init__(self, nazwisko):
        self.nazwisko = nazwisko

liczba_ksiazek = input().strip()
n = int(liczba_ksiazek)
lista_ksiazek = [input().strip(' ') for ksiazka in range(n)]
splitter = []
biblioteka = Biblioteka(10)



for ksiazkaInput in lista_ksiazek:
    usun_nawias = ksiazkaInput.replace("(", "")
    usun_nawias2 = usun_nawias.replace(")", "")
    usun_cudzyslow = usun_nawias2.replace("\"", "")
    splitter = usun_cudzyslow.split(", ")
    ksiazka = Ksiazka(tytul=splitter[0], autor=splitter[1], rok=splitter[2])
    biblioteka.dodaj_egzemplarz_ksiazki(ksiazka)

biblioteka.dostepne_egzemplarze()

