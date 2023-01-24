from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=255,required=True)
    sobrenome = forms.CharField(max_length=255,required=True)
    
    telefone = forms.CharField(widget= forms.TextInput (attrs={'placeholder':'(00)0000-0000'})) 
    
    
    assunto = forms.CharField(widget=forms.Textarea,required=True)
   

  
