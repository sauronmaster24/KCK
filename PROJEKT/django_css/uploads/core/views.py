from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats
import random
import csv
import pandas as pd





###    Funkcyjki wysyłające info    ##########################################
def witaj(request):
    print('Witaj!')
    return render(request, 'witaj.html')


def autorzy(request):
    print('Autorzy')
    return render(request, 'autorzy.html')


def generator(request):
    print('Generuj!')
    wynik = (korwin(tablica_a,tablica_b,tablica_c,tablica_d))
    return render(request, 'generator.html',context = {'gotowe':wynik})




###    Bardzo prosta funkcyjka stanowiąca główny motor napędowy stronki    ###
tablica_a = ["Piotr","Jakub","Natalia"]
tablica_b = ["kocha","szanuje","nienawidzi"]
tablica_c = ["korwina","dżokera","cwela"]
tablica_d = ["z całej siły","niestety...","...żartowałem!",]

def korwin(x,y,z,v):
    los_a = random.choice(x)
    los_b = random.choice(y)
    los_c = random.choice(z)
    los_d = random.choice(v)
    gotowe = str(los_a) + str(" ") + str(los_b) + str(" ") + str(los_c) + str(" ") + str(los_d)
    gotowe = str(gotowe)
    return gotowe
