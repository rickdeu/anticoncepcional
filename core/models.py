from django.db import models
import math
from django.db.models import Avg, Count
from django.db.models import Sum

class Category(models.Model):
    category=models.CharField(verbose_name="Categoria", max_length=250)
    foto = models.ImageField(upload_to='categoria/', verbose_name='Categória', blank=True, null=True)

    def __str__(self):
        return self.category
        


    class Meta:
        ordering = ['category']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Anti(models.Model):
    name=models.CharField(verbose_name="Método", max_length=250)
    eficacia=models.IntegerField(verbose_name="Eficacia", default=1)
    regime=models.CharField(verbose_name="Regime", default="Permanente", max_length=100)
    pros=models.TextField(verbose_name="Prós", max_length=500)
    contra=models.TextField(verbose_name="Contra", max_length=500)
    foto = models.ImageField(upload_to='images/', blank=True, null=True)
    descurta=models.TextField(verbose_name="Descrição curta", max_length=500)
    deslonga=models.TextField(verbose_name="Descrição longa", max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = 'Anticoncepcional'
        verbose_name_plural = 'anticoncepcionais'

class Regra(models.Model):
    anti = models.ForeignKey(Anti, on_delete=models.CASCADE, verbose_name="Método")
    pergunta=models.CharField(verbose_name="Pergunta", default='', max_length=250)
    regra=models.BooleanField(verbose_name="Resposta",default=False)
    def __str__(self):
        return "Regra #"+str(self.id)
    class Meta:
        ordering = ['id']
        verbose_name = 'Regra'
        verbose_name_plural = 'Regras'


class Resposta(models.Model):
    resposta=models.BooleanField(verbose_name="Resposta", max_length=250)
    obs=models.TextField(verbose_name="Observação", max_length=2000)
    regra = models.ForeignKey(Regra, on_delete=models.CASCADE, verbose_name="Regra")
    def __str__(self):
        return self.resposta
    class Meta:
        ordering = ['resposta']
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        


class Pergunta(models.Model):
    metodo=models.ForeignKey(Anti, on_delete=models.CASCADE, default=1)
    #perguntas relativa aos anticoncepcionais orais combinados
    # as duas primerias perguntas valem para as perguntas relativa a pilula só de Progestógeno
    # as perguntas2 de  1, 2, 3, 4, 5, 7
    p1=models.CharField(verbose_name="Você teve bebê nas últimas três semanas?", choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=200, default="")
    p2=models.CharField(verbose_name="Voce está amamentando?", choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    
    p3=models.CharField(verbose_name="Você fuma cigarros?", choices=[('SIM FUMO (1 há 5)', 'SIM FUMO (1 há 5)'), ('SIM FUMO (5 há 10)', 'SIM FUMO (5 há 10)'),('SIM FUMO (10 há 20)', 'SIM FUMO (10 há 20)'), ('NÃO, NÃO FUMO', 'NÃO, NÃO FUMO'),],  max_length=200, default="")

    p4=models.CharField(verbose_name="Você tem cirrose no fígado? ", choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'), ('NÃO SEI', 'NÃO SEI'), ('TALVEZ', 'TALVEZ'),],  max_length=200, default="")
  
    p5=models.CharField(verbose_name="Voce tem algum tumor hepático?", choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'), ('NÃO SEI', 'NÃO SEI'), ('TALVEZ', 'TALVEZ'),],  max_length=200, default="")
  
    p6=models.CharField(verbose_name="Você tem tensão arterial ?", choices=[('SIM (TENHO PRESSÃO ALTA)', 'SIM (TENHO PRESSÃO ALTA)'), ('SIM (TENHO PRESSÃO BAIXA)', 'SIM (TENHO PRESSÃO BAIXA)'), ('NÃO (NÃO TENHO)', 'NÃO (NÃO TENHO)'), ('NÃO SEI', 'NÃO SEI'),],  max_length=200, default="")

    p7=models.CharField(verbose_name="Você tem diabetes ?", choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")

    p8=models.CharField(verbose_name="Você tem doença da vesícula biliar?",  choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'),],  max_length=200, default="")
    
    p9=models.CharField(verbose_name="Você toma medicação para alguma doença crônica?", choices=[('sim', 'SIM'), ('não', 'NÃO')],  max_length=200, default="")
    
    p10=models.CharField(verbose_name="Você já teve um derrame? ", choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=200, default="")

    p11=models.CharField(verbose_name="Você ja teve um coágulo sangüíneo em seus pulmões?", choices=[('SIM (JÁ TIVE)', 'SIM (JÁ TIVE)'), ('NÃO (NUNCA TIVE)', 'NÃO (NUNCA TIVE)')],  max_length=200, default="")
    p12=models.CharField(verbose_name="Você ja teve um coágulo sangüíneo em seuas pernas", choices=[('SIM (JÁ TIVE)', 'SIM (JÁ TIVE)'), ('NÃO (NUNCA TIVE)', 'NÃO (NUNCA TIVE)')],  max_length=200, default="")
    #perguntas relativa a pilula só de Progestógeno
    p13=models.CharField(verbose_name="Você tem  câncer de mama?" , choices=[('TENHO', 'TENHO'), ('SIM (JÁ TIVE)', 'SIM (JÁ TIVE)'), ('NÃO (NUNCA TIVE)', 'NÃO (NUNCA TIVE)')],  max_length=200, default="")
    p14=models.CharField(verbose_name="Você tem sangramento vaginal fora da menstruação?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    #Novas perguntas
    p15=models.CharField(verbose_name="Você tem uma vida sexual ativa?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    p16=models.CharField(verbose_name="Você  faz sexo casual?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    p17=models.CharField(verbose_name="Você tem mais de um parceiro sexual?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    p18=models.CharField(verbose_name="Você pretende engravidar dentro de quanto tempo?" , choices=[('DENTRO DE 6 MESES', 'DENTRO DE 6 MESES'), ('DENTRO DE 1 ANO', 'DENTRO DE 1 ANO'), ('DENTRO DE 2 ANOS', 'DENTRO DE 2 ANOS'), ('DENTRO DE 3 À 5 ANOS', 'DENTRO DE 3 À 5 ANOS')],  max_length=200, default="")
    p19=models.CharField(verbose_name="Você é alérgico(a) a perservativo?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    p20=models.CharField(verbose_name="Práticas alguma atividade física?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    p21=models.CharField(verbose_name="Qual foi a data do último parto?" , choices=[('6 MESES', '6 MESES'), ('1 ANO', '1 ANO'), ('2 ANOS', '2 ANOS'), ('3 ANOS OU MAIS', '3 ANOS OU MAIS')],  max_length=200, default="")
    p22=models.CharField(verbose_name="Com que frequência  consomes bebidas alcoólica?" , choices=[('DE FORMA MODERADA', 'DE FORMA MODERADA'), ('COM BASTANTE FREQUÊNCIA', 'COM BASTANTE FREQUÊNCIA'), ('NÃO CONSUMO', 'NÃO CONSUMO')],  max_length=200, default="")
    p23=models.CharField(verbose_name="Você teve algum enfermidade no fígado?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    p24=models.CharField(verbose_name="Você já teve uma AVC?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    p25=models.CharField(verbose_name="Você tem antecedentes de câncer na família?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    p26=models.CharField(verbose_name="Você tem mais de um parceiro sexual?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")

   
   
   
   
   
    similaridade=models.IntegerField(default=0, verbose_name='RESULTADO')

    def __str__(self):
        return self.metodo.name

    def resultado(self, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26):
        if(self.p1=="SIM"):
            p1=5
        elif(self.p1=="NÃO"):
            p1=2.5
        else:
            p1=1

        if(self.p2=="SIM"):
            p2=5
        elif(self.p2=="NÃO"):
            p2=2.5
        else:
            p2=0

        if(self.p3=="SIM FUMO (1 há 5)"):
            p3=1.5
        elif(self.p3=="SIM FUMO (5 há 10)"):
            p3=2.5        
        elif(self.p3=="SIM FUMO (10 há 20)"):
            p3=5
        elif(self.p3=="NÃO, NÃO FUMO"):
            p3=0 
        else:
            p3=0

        if(self.p4=="SIM"):
            p4=5
        elif(self.p4=="NÃO"):
            p4=0           
        elif(self.p4=="NÃO SEI"):
            p4=1.25
        elif(self.p4=="TALVEZ"):
            p4=2
        else:
            self.p4=0

        if(self.p5=="SIM"):
            p5=5
        elif(self.p5=="NÃO"):
            p5=0           
        elif(self.p5=="NÃO SEI"):
            p5=1.25
        elif(self.p5=="TALVEZ"):
            p5=2.5
        else:
            p5=0

        if(self.p6=="SIM (TENHO PRESSÃO ALTA)"):
            p6=5
        elif(self.p6=="SIM (TENHO PRESSÃO BAIXA)"):
            p6=5   
        elif(self.p6=="NÃO (NÃO TENHO)"):
            p6=0
        elif(self.p6=="NÃO SEI"):
            p6=2.5
        else:
            p6=0

        if(self.p7=="SIM"):
            p7=5
        elif(self.p7=="NÃO"):
            p7=0           
        else:
            p7=0
       
        if(self.p8=="SIM"):
            p8=5
        elif(self.p8=="NÃO"):
            p8=0
        else:
            p8=0

        if(self.p9=="SIM"):
            p9=5
        elif(self.p9=="NÃO"):
            p9=0
        else:
            p9=0

        if(self.p10=="SIM"):
            p10=5
        elif(self.p10=="NÃO"):
            p10=0
        else:
            p10=0


        if(self.p11=="SIM (JÁ TIVE)"):
            p11=5
        elif(self.p11=="NÃO (NUNCA TIVE)"):
            p11=0
        else:
            p11=0

        if(self.p12=="SIM (JÁ TIVE)"):
            p12=5
        elif(self.p12=="NÃO (NUNCA TIVE)"):
            p12=0
        else:
            p12=0

        if(self.p13=="TENHO"):
            p13=5
        elif(self.p13=="SIM (JÁ TIVE)"):
            p13=2.5          
        elif(self.p13=="NÃO (NUNCA TIVE)"):
            p13=0
        else:
            p13=0
        if(self.p14=="SIM"):
            p14=5
        elif(self.p14=="NÃO"):
            p14=0
        else:
            p14=0
        if(self.p15=="SIM"):
            p15=5
        elif(self.p15=="NÃO"):
            p15=0
        else:
            p15=0
 
        if(self.p16=="SIM"):
            p16=5
        elif(self.p16=="NÃO"):
            p16=0
        else:
            p16=0
        
        if(self.p17=="SIM"):
            p17=5
        elif(self.p17=="NÃO"):
            p17=0
        else:
            p17=0
 

        if(self.p18=="DENTRO DE 6 MESES'"):
            p18=5
        elif(self.p18=="DENTRO DE 1 ANO"):
            p18=4   
        elif(self.p18=="DENTRO DE 2 ANOS"):
            p18=3
        elif(self.p18=="DENTRO DE 3 À 5 ANOS"):
            p18=2
        else:
            p18=0
       
        if(self.p19=="SIM"):
            p19=5
        elif(self.p19=="NÃO"):
            p19=0
        else:
            p19=0

        if(self.p20=="SIM"):
            p20=5
        elif(self.p20=="NÃO"):
            p20=0
        else:
            p20=0
   
  
        if(self.p21=="6 MESES"):
            p21=5
        elif(self.p21=="1 ANO"):
            p21=4   
        elif(self.p21=="2 ANOS"):
            p21=3
        elif(self.p18=="3 ANOS OU MAIS"):
            p21=2
        else:
            p21=0
       
        if(self.p22=="DE FORMA MODERADA"):
            p22=5
        elif(self.p22=="COM BASTANTE FREQUÊNCIA"):
            p22=4   
        elif(self.p22=="NÃO CONSUMO"):
            p22=3
        else:
            p22=0
       

        if(self.p23=="SIM"):
            p23=5
        elif(self.p23=="NÃO"):
            p23=0
        else:
            p23=0
   

        if(self.p24=="SIM"):
            p24=5
        elif(self.p24=="NÃO"):
            p24=0
        else:
            p24=0
   

        if(self.p25=="SIM"):
            p25=5
        elif(self.p25=="NÃO"):
            p25=0
        else:
            p25=0

        if(self.p26=="SIM"):
            p26=5
        elif(self.p26=="NÃO"):
            p26=0
        else:
            p26=0
   
   

 


        self.similaridade=math.sqrt(
                            (40*(p1-r1)**2)+
                            (25*(p2-r2)**2)+
                            (40*(p3-r3)**2)+
                            (25*(p4-r4)**2)+
                            (19*(p5-r5)**2)+
                            (25*(p6-r6)**2)+
                            (40*(p7-r7)**2)+
                            (25*(p8-r8)**2)+
                            (18*(p9-r9)**2)+
                            (19*(p10-r10)**2)+
                            (22*(p11-r11)**2)+
                            (18*(p12-r12)**2)+
                            (25*(p13-r13)**2)+
                            (18*(p14-r14)**2)+
                            (28*(p15-r15)**2)+
                            (25*(p16-r16)**2)+
                            (40*(p17-r17)**2)+
                            (24*(p18-r18)**2)+
                            (29*(p19-r19)**2)+
                            (25*(p20-r20)**2)+
                            (22*(p21-r21)**2)+
                            (19*(p22-r22)**2)+
                            (25*(p23-r23)**2)+
                            (22*(p24-r24)**2)+
                            (25*(p25-r25)**2)+
                            (40*(p26-r26)**2))
                            

    
        return "%1.0f"%self.similaridade
    
    def total(self):
        sum = Pergunta.objects.aggregate(Sum('similaridade'))['similaridade__sum']
        x=(self.similaridade*100)/sum
        return "%1.2f"%x 
