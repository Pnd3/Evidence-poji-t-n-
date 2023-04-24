
from databaze import Databaze
from vlozdata import Vlozdata
from kontrola import Kontrola


databaze = Databaze.vytvor_databazi()


print("\n---------------------\nEvidence pojistných\n---------------------")
print("\nVyberte si akci:")

program = "Ano"

while program == "Ano":

    a =input("\n1 - Přidat nového pojistného\n2 - Vypsat všechny pojistné\n3 - Vyhledat pojistného\n4 - Konec\n")

    try:
        a = int(a)
    except ValueError:
        a = 0

    if a == 1:
        
        jmeno = input("Zadejte jmeno pojisteneho:")
        if not jmeno.isalpha():
            print("\nZadejte pouze pismena")
            continue

        prijmeni = input("Zadejte prijmeni:")
        if not prijmeni.isalpha():
            print("\nZadejte pouze pismena")
            continue

        tel_cis = input("Zadejte telefoni cislo:")
        if not Kontrola.cisla(tel_cis) or len(tel_cis)!=9:
            print("\nTelefoni cislo musi byt cislo o delce deviti cisel bez mezer")
            continue

        vek = (input("Zadejte vek:"))
        if not Kontrola.cisla(vek):
            print("\nVek musi byt cislo")
            continue

        vlozdata = Vlozdata(jmeno,prijmeni,tel_cis,vek)
        vlozdata.zapis()

    elif a == 2:
        Vlozdata.vypis()

    elif a == 3:
        Vlozdata.vypis_kde()

    elif a == 4:
        program = "ne"
        
    else:
        print("\nZadejte pouze cislo ktere je na vyber")


