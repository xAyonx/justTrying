import locale
locale.setlocale(locale.LC_ALL, 'de_DE')

eingabe = "j"
while eingabe == "j":
    preis = input("Gib bitte den Preis ein:")
    rabat_in_prozent = input("Rabat in %: ")
    preis = locale.atof(preis)
    rabat_in_prozent = locale.atof(rabat_in_prozent)
    rabat_in_euro = (preis / 100) * rabat_in_prozent
    neuer_preis = preis - rabat_in_euro
    print('Preis mit' ,rabat_in_prozent, "% Rabatt ist", neuer_preis,"€")
    zahlung = input('Der Kunde zahlt: ')
    zahlung = locale.atof(zahlung)
    rueckgeld = round(zahlung - neuer_preis) 
    if rueckgeld < 0:
        print(' zu wenig gezahlt '*10)
        break
    else:
        print("Alles klar")
    print( 'Gegeben: ', zahlung,"€", 'Preis: ',neuer_preis,"€")
    print( 'Wechselgeld: ',
            locale.format_string('%.2f' , rueckgeld),"€")
    eingabe = input('bitte "j "  ,damit die Kasse nicht beendet' )

print('Einen schönen Tag')
