from django.shortcuts import render, redirect
from pousada.forms import ContatoForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt   

@csrf_exempt 
def index(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            telefone = form.cleaned_data['telefone']
            assunto = form.cleaned_data['assunto']
 
            
            html = render_to_string('mail/formulario-email.html', {
                'nome':nome,
                'sobrenome':sobrenome,
                'telefone':telefone,
                'assunto':assunto,
            })
            
            send_mail('Informações sobre a reserva para:', '....', 'rincaocomprido@gmail.com' ,['rincaocomprido@gmail.com'], html_message=html,fail_silently=False,),
            
            messages.success(request, 'Email enviado com sucesso, entraremos em contato assim que possível.')
            print(send_mail)
            
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