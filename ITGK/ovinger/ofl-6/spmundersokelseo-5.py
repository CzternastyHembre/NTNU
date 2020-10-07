from sys import exit

# Velkommen til spørreundersøkelsen!

# Hvilket kjønn er du? [f/m]: f
# Hvor gammel er du?: 21
# Tar du et eller flere fag? [ja/nei ]: bleh
# Tar du et eller flere fag? [ja/nei ]: ja
# Tar du ITGK? [ja/nei]: ja
# Hvor mange timer bruker du daglig (i snitt) på lekser?: 2
#['Hvilket kjønn er du? [f/m]: f','Hvor gammel er du?: 21','Tar du et eller flere fag? [ja/nei ]: ','Tar du et eller flere fag? [ja/nei ]: ']
kvinner = 0
menn = 0
tar_fag = 0
tar_itgk = 0
timer_snitt = 0
antall_svar = 0
totalt = [kvinner, menn, tar_fag, tar_itgk, timer_snitt, antall_svar]
svar = []
print('12'.isdigit())
def undersokerlse():
#    global totalt
    global kvinner
    global menn
    global tar_fag
    global tar_itgk
    global timer_snitt
    global antall_svar

    while True:
        print('Velkommen til spørreundersøkelsen!')

        while True:
            kjonn = input('Hvilket kjønn er du? [f/m]: ').lower()
            if kjonn == 'hade':
                exit()
            if kjonn == 'f':
                kvinner1 = 1
                break
            if kjonn == 'm':
                menn1 = 1
                break

        while True:
            alder = input('Hvor gammel er du?: ')
            if alder == 'hade':
                exit()
            if not alder.isdigit():
                print('Skriv inn ett tall')
                continue
            alder = int(alder)
            if 16 <= alder and alder <= 25:
                alder1 = alder
                ugyldig_alder = False
                break
            ugyldig_alder = True
            break

        if ugyldig_alder:
            print('Du kan dessverre ikke ta denne undersøkelsen')
            continue

        while True:
            fag = input('Tar du et eller flere fag? [ja/nei ]: ')
            if fag == 'hade':
                exit()
            if fag == 'ja':
                tar_fag1 = 1
                ikke_ferdig = True
                break
            if fag == 'nei':
                tar_fag1 = 0
                ikke_ferdig = False
                break
        if ikke_ferdig:
            while True:
                itgk = input('Tar du ITGK? [ja/nei]: ')
                if itgk == 'hade':
                    exit()
                if itgk == 'f':
                    kvinner1 = 1
                    break
                if itgk == 'm':
                    menn1 = 1
                    break

        timer = int(input('Hvor mange timer bruker du daglig (i snitt) på lekser?: 2'))



        menn += menn1
        kvinner += kvinner1


undersokerlse()