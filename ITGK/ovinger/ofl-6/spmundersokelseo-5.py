from sys import exit

kvinner = 0
menn = 0
tar_fag = 0
tar_itgk = 0
timer_snitt = 0
timer_array = []
antall_svar = 0

def undersokerlse():
#    global totalt
    global kvinner
    global menn
    global tar_fag
    global tar_itgk
    global timer_snitt
    global antall_svar
    global timer_array

    while True:
        tar_itgk1 = 0
        menn1 = 0
        kvinner1 = 0
        tar_fag1 = 0

        print('Velkommen til spørreundersøkelsen!')

        while True:
            kjonn = input('Hvilket kjønn er du? [f/m]: ').lower()
            if kjonn == 'hade':
                skriv_svar()
            if kjonn == 'f':
                kvinner1 = 1
                break
            if kjonn == 'm':
                menn1 = 1
                break

        while True:
            alder = input('Hvor gammel er du?: ')
            if alder == 'hade':
                skriv_svar()
            if not alder.isdigit():
                print('Skriv inn ett heltall')
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
                skriv_svar()
            if fag == 'ja':
                tar_fag1 = 1
                ikke_ferdig = True
                break
            if fag == 'nei':
                ikke_ferdig = False
                break
        if ikke_ferdig:
            while True:
                spm = 'Tar du ITGK? [ja/nei]: '
                if alder1 >= 22:
                    spm = 'Tar du virkelig ITGK? [ja/nei]: '
                itgk = input(spm)
                if itgk == 'hade':
                    skriv_svar()
                if itgk == 'ja':
                    tar_itgk1 = 1
                    break
                if itgk == 'nei':
                    break
            while True:
                timer = input('Hvor mange timer bruker du daglig (i snitt) på lekser?: ')
                if timer == 'hade':
                    skriv_svar()
                if not timer.isdigit():
                    print('Skriv inn ett heltall')
                    continue
                timer = int(timer)
                timer_array.append(timer)
                break

        kvinner += kvinner1
        menn += menn1
        tar_fag += tar_fag1
        tar_itgk += tar_itgk1
        sum_timer = 0
        for i in timer_array:
            sum_timer += i
        timer_snitt = sum_timer/len(timer_array)
        antall_svar += 1



def skriv_svar():
    print('Resultat av undersøkelse!')
    print('Antall kvinner:', kvinner)
    print('Antall menn:', menn)
    print('Antall personer som tar fag:', tar_fag)
    print('Antall personer som tar ITGK:', tar_itgk)
    print('Antall timer i snitt brukt på lekser :', timer_snitt)
    exit()

undersokerlse()
