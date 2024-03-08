#zadatak 1.4.2
ocjena = float(input("Upisi ocjenu izmedu 0.0 i 1.0: "))

if (ocjena >= 0.9):
    kategorija = "A"

elif (ocjena >=0.8):
    kategorija = "B"

elif (ocjena >=0.7):
    kategorija = "C"

elif (ocjena >=0.6):
    kategorija = "D"

elif (ocjena <0.6):
    kategorija = "F"

print(kategorija)


