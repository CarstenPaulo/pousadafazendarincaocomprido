from django.shortcuts import render, redirect
from pousada.forms import ContatoForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')
            telefone = request.POST.get('telefone')
            email = request.POST.get('email')
            assunto = request.POST.get('assunto')
            
            
            data = {
                'nome':nome,
                'sobrenome':sobrenome,
                'telefone':telefone,
                'email':email,
                'assunto':assunto,
            }        
            
            dados = '''
            
            Nome: {}    
            
            Sobrenome: {}  
            
            Telefone: {}

            Email: {}

            Assunto: {}

            '''.format(data['nome'],data['sobrenome'],data['telefone'],data['email'],data['assunto'])
            send_mail(data['nome'],dados, '', ['rincaocomprido@gmail.com'])
            messages.success(request, 'Email enviado com sucesso, entraremos em contato assim que possível.')
        form = ContatoForm()
    else:
        form = ContatoForm()
    return render(request, 'index.html',{'form':form})

#album da casa
def cozinha(request):
    return render(request, 'cozinha/cozinha.html')

def sala(request):
    return render(request, 'sala/sala.html')

def quartos(request):
    return render(request, 'quartos/quartos.html')

def mezanino(request):
    return render(request, 'mezanino/mezanino.html')

def lazer(request):
    return render(request, 'lazer/lazer.html')


def urubici(request):
    return render (request, 'urubici.html')


def duvidas(request):
    return render (request, 'duvidas.html')