import sqlite3

class Vlozdata():

    def __init__(self,jmeno,prijmeni,tel_cis,vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.tel_cis = tel_cis
        self.vek = vek

    def zapis(self):
        con = sqlite3.connect('projekt_databaze.db')
        cur = con.cursor()
        cur.execute("INSERT INTO uzivatele (jmeno,prijmeni,telefonni_cislo,vek) VALUES (?, ?, ?, ?)", (self.jmeno,self.prijmeni,self.tel_cis,self.vek))
        con.commit()
        input("\nData byla ulozena. Pokracujte libovolnou klavesou...")
        

    def vypis():
        con = sqlite3.connect('projekt_databaze.db')
        cur = con.cursor()
        print("Pojisteni uzivatele")
        cur.execute('SELECT * FROM uzivatele')
        vysledky = cur.fetchall()
        for vysledek in vysledky:
            print(vysledek)
            
        input("\nPokracujte libovolnou klavesou...")

    def vypis_kde():
        con = sqlite3.connect('projekt_databaze.db')
        cur = con.cursor()
        jmeno_vyhledat = input("Zadejte jmeno pojisteneho:")
        prijmeni_vyhledat = input("Zadejte prijmeni:")
        cur.execute("SELECT * FROM uzivatele WHERE jmeno =(?) AND prijmeni = (?)",(jmeno_vyhledat,prijmeni_vyhledat))
        vyhledani = cur.fetchall()
        for vyhled in vyhledani:
            print(vyhledani)
        input("\nPokracujte libovolnou klavesou...")

