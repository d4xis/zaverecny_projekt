from Pojisteny import Pojisteny
 
def vytvorit_pojisteneho():

    ''' Kod pro vytvoreni pojisteneho.'''
    
    jmeno = input('\nZadej jméno: ')
    prijmeni = input('Zadej příjmení: ')
    vek = int(input('Zadej věk: '))
    telefon = input('Zadej telefon: ')
    print("Nový pojištěnec zaevidován.\n")
 
    pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
    pojisteni.append(pojisteny)
 
def vyhledat_pojisteneho():

    ''' Kod pro vyhledani pojisteneho'''

    hledane_jmeno = input('Zadej jméno: ')
    hledane_prijmeni = input('Zadej příjmení: ')
 
    for pojisteny in pojisteni:
        if pojisteny.jmeno == hledane_jmeno and pojisteny.prijmeni == hledane_prijmeni:
            print(str(pojisteny))
            break
    else:
        print('Pojištěný nenalezen, zkuste prosím znovu.')
 
def vypis_pojistenych():

    '''Kod pro vypis seznamu pojistenych'''

    for pojisteny in pojisteni:
        print(str(pojisteny))
 
def main():

    ''' Hlavní část kodu spolu s volbou moznostmi. '''
    
    while True:
        print('==========================\nEVIDENCE POJISTNÉ UDÁLOSTI\n==========================\n')
        volba = input('Zvolte možnost:\n'
            '[1] Vytvořit nového pojištěného\n'
            '[2] Vyhledat pojištěného\n'
            '[3] Vypis pojištěných\n'
            '[4] Konec aplikace\n'
            '\n'
            'Zadej volbu: ')
         
        if volba == '1':
            vytvorit_pojisteneho()
        elif volba == '2':
            vyhledat_pojisteneho()
        elif volba == '3':
            vypis_pojistenych()
        elif volba == '4':
            print('Konec aplikace.\n')
            break
        else:
            print('\nNeplatná volba, zkuste prosím znovu...\n')
 
pojisteni = []
main()