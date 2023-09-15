def gör_något_annat(tal):
    """Vi förväntar oss att tal är en sträng men ett giltligt heltal"""
    tal = int(tal)
    tal+= tal
    tal*=tal

    return tal

def gör_något(tar_in_något):
    print('Vi kör lite kod')
    print(tar_in_något)
    # print(f'{tar_in_något}')

    return 2*tar_in_något

def skriv_ut_huvud_meny():
    print("1. Vi gör något")
    print("2. Vi gör något annat")
    print("3. Avsluta")

def huvudmeny():
    while True:
        skriv_ut_huvud_meny()
        val =  input('Gör ett val: ')
        #-------------------------------------------------
        if val == "1":
            att_göra = input('Vad ska vi göra?: ')
            tar_emot_ett_värde = gör_något(att_göra)
            if tar_emot_ett_värde != '':
                print(tar_emot_ett_värde)
            else:
                print('Vi fick inget tillbaka!!')
        #-------------------------------------------------
        elif val == "2":
            nummer = input('Skriv in ett heltal: ')

            if nummer.isdigit():
                tar_emot_värde = gör_något_annat(nummer)
                print(tar_emot_värde)
            else:
                print('Fel format!')
        #-------------------------------------------------
        elif val == "3":
            break
        #-------------------------------------------------
        else:
            print('Fel val!!!!')


if __name__ == "__main__":
    huvudmeny()
    print('Den här koden körs!!')