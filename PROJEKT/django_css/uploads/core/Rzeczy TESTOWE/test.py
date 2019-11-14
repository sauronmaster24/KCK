import random

tablica0 = ["Piotr","Jakub","Natalia"]
tablica1 = ["kocha","szanuje","nienawidzi"]
tablica2 = ["korwina","dżokera","cwela"]
tablica3 = ["z całej siły","niestety...","...żartowałem!",]

def korwin(nazwa_tab,liczba_tab):
    gotowe = ''
    for i in range(0,int(liczba_tab)-1):
        which = str(nazwa_tab) + str(i)
        los = random.choice(which)
        gotowe = str(gotowe) + str(los)
    return gotowe

print(korwin("tablica",4))
