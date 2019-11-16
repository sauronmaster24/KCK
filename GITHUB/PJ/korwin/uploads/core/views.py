from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats
import random
import csv
import pandas as pd



###########       Funkcyjki wysyłające info, używające django:    #############


def witaj(request):
    print('Witaj!')
    return render(request, 'witaj.html')


def autorzy(request):
    print('Autorzy')
    return render(request, 'autorzy.html')


### [Ta funkcyjka używa funkcji generujacej teksty i wysyła stringa do html
### używając django.]

def generator(request):
    print('Generuj!')
    wynik = (korwin(tablica))
    return render(request, 'generator.html',context = {'gotowe':wynik})


###    Bardzo prosta funkcyjka stanowiąca główny motor napędowy stronki    ###
######      [ Każdy wiersz w tablicy to kolejna kolumna w memie ]       ######


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
