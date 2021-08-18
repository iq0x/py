print ("versandkosten");

gewicht = float(input("kg: "))

print("gewicht: ", gewicht)

if gewicht > 20:
    print("das paket ist zu gross")
else:
    if gewicht >= 10:
        print("14 euro")
    elif gewicht >= 5:
        print("10,50Euro")
    else:
        print("7Euro")
