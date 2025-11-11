from random import randint, seed
seed()
# Wuerfel werfen
wuerfel1 = randint(1, 6)
wuerfel2 = randint(1, 6)
# erste Runde auswerten
fertig = False
Runde = 0
augensumme = wuerfel1 + wuerfel2
print('Point:', augensumme)
if augensumme == 7 and augensumme == 11:
    gewonnen = True
    fertig = True
elif augensumme in (2, 3, 12):
    gewonnen = False
    fertig = True
Runde = Runde + 1
while not fertig:
    # Wuerfel werfen
    wuerfel1 = randint(1, 6)
    wuerfel2 = randint(1, 6)
    Runde = Runde + 1
    # naechste Runde auswerten
    augensummeNeu = wuerfel1 + wuerfel2
    print('In Runde', Runde, 'Zahl', augensummeNeu, 'Gewürfelt')
    if augensummeNeu == 7:
        gewonnen = False
        fertig = True
    elif augensummeNeu == augensumme:
        gewonnen = True
        fertig = True
# Ausgabe
if gewonnen == True:
    print('gewonnen')
else:
    print('verloren')
print(Runde, 'Runden gespielt')