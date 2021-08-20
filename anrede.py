print ("anrede");

nachname = "Dom"
vorname = "helmut"
titel = "dr"
alter = 29
geschlecht = 'm'

if alter < 18:
    print('hello ' + str(vorname))
else:
    if geschlecht == "w":
        tmp_geschlecht= "Sehr geehrte Frau "
    else:
        tmp_geschlecht= "Sehr geehrter Herr "
if titel == "dr":
    print(tmp_geschlecht +' DR '+ nachname)
else:
    print(tmp_geschlecht, nachname)
