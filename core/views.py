from django.shortcuts import render, redirect, reverse, get_object_or_404
from core.models import *
from core.forms import *
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

def home(request,*args, **kwargs):
    anti=Anti.objects.all()[:4]
    cat=Category.objects.all()[:8]
    regra=Regra.objects.all()
    form = AntiForm
    if request.method == 'POST':
	    form = AntiForm(request.POST)
	    if form.is_valid():
            #perguntas 1
                p1 = form.cleaned_data['p1']
                p2 = form.cleaned_data['p2']
                p3 = form.cleaned_data['p3']
                p4 = form.cleaned_data['p4']
                p5 = form.cleaned_data['p5']
                p6 = form.cleaned_data['p6']
                p7 = form.cleaned_data['p7']
                p8 = form.cleaned_data['p8']
                p9 = form.cleaned_data['p9']
                p10 = form.cleaned_data['p10']
                #perguntas 2
                p11 = form.cleaned_data['p11']
                p12 = form.cleaned_data['p12']
                p13 = form.cleaned_data['p13']
                #perguntas 2
                p14 = form.cleaned_data['p14']
                p15 = form.cleaned_data['p15']
                p16 = form.cleaned_data['p16']
                p17 = form.cleaned_data['p17']
                p18 = form.cleaned_data['p18']
                p19 = form.cleaned_data['p19']
                p20 = form.cleaned_data['p20']
                p21 = form.cleaned_data['p21']
                p22 = form.cleaned_data['p22']
                p23 = form.cleaned_data['p23']
                p24 = form.cleaned_data['p24']
                p25 = form.cleaned_data['p25']
                p26 = form.cleaned_data['p26']

                if(p1=="SIM"):
                    p1=5
                elif(p1=="NÃO"):
                    p1=0
                else:
                    p1=0

                if(p2=="SIM"):
                    p2=5
                elif(p2=="NÃO"):
                    p2=0
                else:
                    p2=0

                if(p3=="SIM FUMO (1 há 5)"):
                    p3=1.25
                elif(p3=="SIM FUMO (5 há 10)"):
                    p3=2.5          
                elif(p3=="SIM FUMO (10 há 20)"):
                    p3=5
                elif(p3=="NÃO, NÃO FUMO"):
                    p3=0 
                else:
                    p3=0

                if(p4=="SIM"):
                    p4=5
                elif(p4=="NÃO"):
                    p4=0           
                elif(p4=="NÃO SEI"):
                    p4=1.25
                elif(p4=="TALVEZ"):
                    p4=2.5
                else:
                    p4=0

                if(p5=="SIM"):
                    p5=5
                elif(p5=="NÃO"):
                    p5=0           
                elif(p5=="NÃO SEI"):
                    p5=1.25
                elif(p5=="TALVEZ"):
                    p5=2.5
                else:
                    p5=0

                if(p6=="SIM (TENHO PRESSÃO ALTA)"):
                    p6=5
                elif(p6=="SIM (TENHO PRESSÃO BAIXA)"):
                    p6=5   
                elif(p6=="NÃO (NÃO TENHO)"):
                    p6=0
                elif(p6=="NÃO SEI"):
                    p6=2.25
                else:
                    p6=0

                if(p7=="SIM"):
                    p7=5
                elif(p7=="NÃO"):
                    p7=0           
                else:
                    p7=0
            
                if(p8=="SIM"):
                    p8=5
                elif(p8=="NÃO"):
                    p8=0
                else:
                    p8=0

                if(p9=="SIM"):
                    p9=5
                elif(p9=="NÃO"):
                    p9=0
                else:
                    p9=0

                if(p10=="SIM"):
                    p10=5
                elif(p10=="NÃO"):
                    p10=0
                else:
                    p10=0


                if(p11=="SIM (JÁ TIVE)"):
                    p11=5
                elif(p11=="NÃO (NUNCA TIVE)"):
                    p11=0
                else:
                    p11=0

                if(p12=="SIM (JÁ TIVE)"):
                    p12=5
                elif(p12=="NÃO (NUNCA TIVE)"):
                    p12=0
                else:
                    p12=0

                if(p13=="TENHO"):
                    p13=5
                elif(p13=="SIM (JÁ TIVE)"):
                    p13=2.5          
                elif(p13=="NÃO (NUNCA TIVE)"):
                    p13=0
                else:
                    p13=0

                if(p14=="SIM"):
                    p14=5
                elif(p14=="NÃO"):
                    p14=0
                else:
                    p14=0
                #Novas perguntas
                if(p15=="SIM"):
                    p15=5
                elif(p15=="NÃO"):
                    p15=0
                else:
                    p15=0
        
                if(p16=="SIM"):
                    p16=5
                elif(p16=="NÃO"):
                    p16=0
                else:
                    p16=0
                
                if(p17=="SIM"):
                    p17=5
                elif(p17=="NÃO"):
                    p17=0
                else:
                    p17=0
        

                if(p18=="DENTRO DE 6 MESES'"):
                    p18=5
                elif(p18=="DENTRO DE 1 ANO"):
                    p18=4   
                elif(p18=="DENTRO DE 2 ANOS"):
                    p18=3
                elif(p18=="DENTRO DE 3 À 5 ANOS"):
                    p18=2
                else:
                    p18=0
            
                if(p19=="SIM"):
                    p19=5
                elif(p19=="NÃO"):
                    p19=0
                else:
                    p19=0

                if(p20=="SIM"):
                    p20=5
                elif(p20=="NÃO"):
                    p20=0
                else:
                    p20=0
        
        
                if(p21=="6 MESES"):
                    p21=5
                elif(p21=="1 ANO"):
                    p21=4   
                elif(p21=="2 ANOS"):
                    p21=3
                elif(p18=="3 ANOS OU MAIS"):
                    p21=2
                else:
                    p21=0
            
                if(p22=="DE FORMA MODERADA"):
                    p22=5
                elif(p22=="COM BASTANTE FREQUÊNCIA"):
                    p22=4   
                elif(p22=="NÃO CONSUMO"):
                    p22=3
                else:
                    p22=0
            

                if(p23=="SIM"):
                    p23=5
                elif(p23=="NÃO"):
                    p23=0
                else:
                    p23=0
        

                if(p24=="SIM"):
                    p24=5
                elif(p24=="NÃO"):
                    p24=0
                else:
                    p24=0
        

                if(p25=="SIM"):
                    p25=5
                elif(p25=="NÃO"):
                    p25=0
                else:
                    p25=0

                if(p26=="SIM"):
                    p26=5
                elif(p26=="NÃO"):
                    p26=0
                else:
                    p26=0
   



                pegunta = Pergunta.objects.all()
                if (pegunta):
                    for pegunta in pegunta:
                        pegunta.similaridade=pegunta.resultado(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26)
                        pegunta.save()

                context={'anti':anti, 'cat':cat, 'regra':regra}
                #return render(request,template_name, context) 
                #return redirect('core:resultado_teste')
                return redirect(reverse('core:resultado_teste'))




    template_name='core/index_new.html'
    context={'anti':anti, 'cat':cat,'form':form}
    return  render(request, template_name, context)

def second_home(request,*args, **kwargs):
    anti=Anti.objects.all()
    cat=Category.objects.all()

    template_name='core/dashboard.html'
    context={'anti':anti, 'cat':cat}
    return  render(request, template_name, context)

def anti(request,*args, **kwargs):

    anti=Anti.objects.all()
    cat=Category.objects.all()

    template_name='core/dashboard.html'
    context={'anti':anti, 'cat':cat}
    return  render(request, template_name, context)

def choose(request,*args, **kwargs):
    regra=Regra.objects.all()
    anti=Anti.objects.all()
    cat=Category.objects.all()
    template_name='core/choose.html'
    form = RegraForm()


    if request.method == 'POST':
	    form = RegraForm(request.POST)
	    if form.is_valid():
                context={'anti':anti, 'cat':cat, 'regra':regra}
                return render(request,template_name, context) 




    context={'anti':anti, 'cat':cat, 'regra':regra,'form':form}
    return  render(request, template_name, context)


def second_choose(request,*args, **kwargs):
    resultado="Pílulas Anticoncepcionais de Emergência"
    regra=Regra.objects.all()
    anti=Anti.objects.all()
    cat=Category.objects.all()
    template_name='core/ashion/formulario_teste.html'
    form = AntiForm
    if request.method == 'POST':
	    form = AntiForm(request.POST)
	    if form.is_valid():
            #perguntas 1
                p1 = form.cleaned_data['p1']
                p2 = form.cleaned_data['p2']
                p3 = form.cleaned_data['p3']
                p4 = form.cleaned_data['p4']
                p5 = form.cleaned_data['p5']
                p6 = form.cleaned_data['p6']
                p7 = form.cleaned_data['p7']
                p8 = form.cleaned_data['p8']
                p9 = form.cleaned_data['p9']
                p10 = form.cleaned_data['p10']
                #perguntas 2
                p12 = form.cleaned_data['p12']
                p13 = form.cleaned_data['p13']
                p14 = form.cleaned_data['p14']

                #perguntas 2
                p21 = form.cleaned_data['p21']
                p22 = form.cleaned_data['p22']
                #perguntas 2
                p31 = form.cleaned_data['p31']
                p32 = form.cleaned_data['p32']

                if(not p1 and not p2 and not p3 and not p4 and not p5 and not p6 and not p7 and not p8 and not p9 and not p10):
                    resultado="Anticoncepcionais Orais Combinados "
                elif(not p1 and not p2 and not p12 and not p13 and not p14):
                    resultado="Pílulas Só de Progestógeno"
                elif(not p1 and not p4 and not p5 and not p6 and not p8 and not p21 and not p9 and not p22):
                    resultado="Injetáveis Só de Progestógeno"
                elif(not p31 and not p1 and not p2 and not p32 and not p4 and not p5 and not p6 and not p8 and not p9 and not p10):
                    resultado="Injetáveis Mensais"
                else:
                    resultado="Pílulas Anticoncepcionais de Emergência"
      





            
                context={'anti':anti, 'cat':cat, 'regra':regra}
                #return render(request,template_name, context) 
                #return redirect('core:resultado_teste')
                return redirect(reverse('core:resultado_teste', args=(resultado, )))

 


    context={'anti':anti, 'cat':cat, 'regra':regra,'form':form}
    return  render(request, template_name, context)


def resultado_teste(request,*args, **kwargs):
    resposta=Resposta.objects.all()
    anti=Pergunta.objects.order_by('-similaridade').all()#[:8]#filter(category__category=category)
    cat=Category.objects.all()
    template_name='core/response_new.html'
    context={'anti':anti, 'cat':cat, 'resposta':resposta}
    return  render(request, template_name, context)

def detalhes_resultado_teste(request, pk,*args, **kwargs):
    obj = get_object_or_404(Anti, pk=pk)
    resposta=Resposta.objects.all()
    anti=Anti.objects.all()
    cat=Category.objects.all()
    template_name='core/ashion/resultado_detail.html'
    context={'anti':anti, 'cat':cat, 'resposta':resposta, 'obj':obj}
    return  render(request, template_name, context)
