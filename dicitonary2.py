dict_lösenord = {'9912041234':'1234',
                 '9004121212':'pwd',
                 '0105225555':'password'}


dict_lösenord['0411284441'] = 'Hejsan123'
dict_lösenord[8510015534] = 'Bananer'
print(dict_lösenord)

for personnummer, lösenord in dict_lösenord.items():
    print(personnummer,lösenord, sep=' har lösenord --> ')

for personnummer in dict_lösenord:
    lösenord = dict_lösenord[personnummer]
    print(personnummer,lösenord, sep=' har lösenord --> ')