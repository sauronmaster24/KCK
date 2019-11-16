import random

#każdy wiesz to kolejna kolumna w memie
tablica = [
["Piotr","Jakub","Natalia"],
["kocha","szanuje","nienawidzi"],
["korwina","dżokera","cwela"],
["z całej siły","niestety...","...żartowałem!"]
]

def korwin(x):
    gotowe = ''
    for i in range(0,len(x)):
        tekst = random.choice(x[i])
        gotowe = gotowe + tekst + " "
    gotowe = str(gotowe)
    return gotowe

print(korwin(tablica))
