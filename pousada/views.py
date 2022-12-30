from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

#album da casa
def cozinha(request):
    return render(request, 'cozinha/cozinha.html')

def sala(request):
    return render(request, 'sala/sala.html')

def quartos(request):
    return render(request, 'quartos/quartos.html')

def lazer(request):
    return render(request, 'lazer/lazer.html')


def urubici(request):
    return render (request, 'urubici.html')


def duvidas(request):
    return render (request, 'duvidas.html')