#zadatak 1.4.2
def ocjenjivanje(ocjena):
    if (ocjena >= 0.9):
        return "A"

    elif (ocjena >=0.8):
        return "B"

    elif (ocjena >=0.7):
        return "C"

    elif (ocjena >=0.6):
        return "D"

    elif (ocjena <0.6):
        return "F"

try:
    ocjena = float(input("Upisi ocjenu izmedu 0.0 i 1.0: "))
    if isinstance(ocjena, (float)):
        if 0.0 <= ocjena <= 1.0:
            kategorija = ocjenjivanje(ocjena)
            print("Ocjena = ", kategorija)
        else:
            print("Ocjena izvan intervala 0.0 i 1.0")
    else:
        print("Uneseni podatak nije broj.")
except ValueError:
    print("Uneseni podatak nije broj")

