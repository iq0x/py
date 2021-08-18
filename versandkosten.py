print ("versandkosten");

gewicht = float(input("kg: "))

print("gewicht: ", gewicht)

if gewicht > 20:
    print("das paket ist zu gross")
else:
    if gewicht >= 10:
        preis = 14
    elif gewicht >= 5:
        preis = 10.50
    else:
        preis = 7

    print(preis)
