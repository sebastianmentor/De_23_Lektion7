# Logga in med personummer och lösenord!
personnummer_och_lösenord = {"9501015555":"password"}

def logga_in(p_nummer):
    if p_nummer in personnummer_och_lösenord:
        lösenord = input('Skriv in lösenordet: ')
        if personnummer_och_lösenord[p_nummer] == lösenord:
            print('Grattis du är inloggad!!')
        else:
            print('Inte korrekt lösenord!')
    
    else:
        print("Hej ny användare!")
        ny_anv_lösenord = input('Vänligen skriv in ditt lösenord!')
        personnummer_och_lösenord[p_nummer] = ny_anv_lösenord
    


def main():
    while True:
        print('Logga in med ditt personnummer eller avsluta med q!')
        print('Format 10 siffrigt!!')
        personnummer =  input('>>>')
        if personnummer == 'q':
            break
        elif personnummer.isdigit():
            if len(personnummer) != 10:
                print('Fel inmatat!!!')
                continue
            else:
                logga_in(personnummer)
        else:
            print('Skriv in ett personnummer!!')
    


if __name__ == "__main__":
    main()