from recap_funktioner import gör_något_annat

heltal = input("Skriv in ett heltal: ")

if heltal.isdigit():
    print(gör_något_annat(heltal))
else:
    print('Sorry, fel inmatning! Programmet avslutas!!')