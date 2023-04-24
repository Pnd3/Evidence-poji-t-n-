

import sqlite3

class Databaze:
    
    def vytvor_databazi():

        con = sqlite3.connect('projekt_databaze.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS uzivatele
               (jmeno text, prijmeni text, telefonni_cislo integer, vek integer)''')
        con.commit()
        


    
       

