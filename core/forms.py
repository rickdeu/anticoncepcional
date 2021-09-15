from django import forms
#from django.forms import ModelForm
from core.models import * 

#Reutilizacao da entidade para criacao do formulario
class RegraForm(forms.ModelForm):
    regra = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'checkbox','class': 'form-control'}
        ),
        max_length=30, 
        required=True, 
        help_text='Regra',
        label='Regra'
        )
    class Meta:
        model=Regra
        fields = ['regra',]



#P1= [('sim', 'SIM'), ('não', 'Não'),]
class AntiForm(forms.ModelForm):
    """p1 = forms.CharField(label='Você teve bebê nas últimas três semanas?', required=True, 
        widget=forms.RadioSelect(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')]),)
    p2 = forms.CharField(label='Voce está amamentando?', required=True,
        widget=forms.RadioSelect(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')]))
    p3 = forms.CharField(label='Você fuma cigarros?', required=True,
        widget=forms.RadioSelect(choices=[('SIM FUMO (1 há 5)', 'SIM FUMO (1 há 5)'), ('SIM FUMO (5 há 10)', 'SIM FUMO (5 há 10)'),('SIM FUMO (10 há 20)', 'SIM FUMO (10 há 20)'), ('NÃO, NÃO FUMO', 'NÃO, NÃO FUMO'),]))
    
    p4 = forms.CharField(label='Você tem cirrose no fígado? ', required=True,
        widget=forms.RadioSelect(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'), ('NÃO SEI', 'NÃO SEI'), ('TALVEZ', 'TALVEZ'),]))
    p5 = forms.CharField(label='Voce tem algum tumor hepático?', required=True,
        widget=forms.RadioSelect(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'), ('NÃO SEI', 'NÃO SEI'), ('TALVEZ', 'TALVEZ'),]))
  
    p6 = forms.CharField(label='Você tem pressão arterial ?', required=True,
        widget=forms.RadioSelect(choices=[('SIM (TENHO PRESSÃO ALTA)', 'SIM (TENHO PRESSÃO ALTA)'), ('SIM (TENHO PRESSÃO BAIXA)', 'SIM (TENHO PRESSÃO BAIXA)'), ('NÃO (NÃO TENHO)', 'NÃO (NÃO TENHO)'), ('NÃO SEI', 'NÃO SEI'),]))

    p7 = forms.CharField(label='Você já teve diabetes ?', required=True,
        widget=forms.RadioSelect(choices=[('SIM TENHO', 'SIM TENHO'), ('NÃO TENHO', 'NÃO TENHO'), ('JÁ TIVE', 'JÁ TIVE'),]))

    p8 = forms.CharField(label='Você tem doença da vesícula biliar?', required=True,
        widget=forms.RadioSelect(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'),]))

    p9 = forms.CharField(label='Você toma medicação para alguma doença cronica?', required=True,
        widget=forms.RadioSelect(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')]))

    p10 = forms.CharField(label='Você já teve um derrame? ', required=True,
        widget=forms.RadioSelect(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')]))


    p11 = forms.CharField(label='Você ja teve um coágulo sangüíneo em seus pulmões?', required=True,
        widget=forms.RadioSelect(choices=[('SIM (JÁ TIVE)', 'SIM (JÁ TIVE)'), ('NÃO (NUNCA TIVE)', 'NÃO (NUNCA TIVE)')]))

    p12 = forms.CharField(label='Você ja teve um coágulo sangüíneo em seuas pernas', required=True,
        widget=forms.RadioSelect(choices=[('SIM (JÁ TIVE)', 'SIM (JÁ TIVE)'), ('NÃO (NUNCA TIVE)', 'NÃO (NUNCA TIVE)')]))

    p13 = forms.CharField(label='Você tem  câncer de mama?', required=True,
        widget=forms.RadioSelect(choices=[('TENHO', 'TENHO'), ('SIM (JÁ TIVE)', 'SIM (JÁ TIVE)'), ('NÃO (NUNCA TIVE)', 'NÃO (NUNCA TIVE)')]))

    p14 = forms.CharField(label='Você tem sangramento vaginal?', required=True,
        widget=forms.RadioSelect(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'),]))"""



   


    class Meta:
        model=Pergunta
        fields = ['p1', 'p18', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26']
        #exclude=['metodo', 'similaridade']

