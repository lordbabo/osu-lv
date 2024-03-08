#zadatak 1.4.1
def total_euro(sati, satnica) :
    zarada = sati * satnica
    return zarada

sati = float(input("Unesite broj radnih sati: "))
satnica = float(input("Unesi satnicu: "))

ukupno = total_euro(sati, satnica)
print(ukupno)

