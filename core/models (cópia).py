from django.db import models
import math

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
    eficacia=models.CharField(verbose_name="Eficacia", max_length=100)
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
  
    p6=models.CharField(verbose_name="Você tem pressão arterial ?", choices=[('SIM (TENHO PRESSÃO ALTA)', 'SIM (TENHO PRESSÃO ALTA)'), ('SIM (TENHO PRESSÃO BAIXA)', 'SIM (TENHO PRESSÃO BAIXA)'), ('NÃO (NÃO TENHO)', 'NÃO (NÃO TENHO)'), ('NÃO SEI', 'NÃO SEI'),],  max_length=200, default="")

    p7=models.CharField(verbose_name="Você já teve diabetes ?", choices=[('SIM TENHO', 'SIM TENHO'), ('NÃO TENHO', 'NÃO TENHO'), ('JÁ TIVE', 'JÁ TIVE'),],  max_length=200, default="")

    p8=models.CharField(verbose_name="Você tem doença da vesícula biliar?",  choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'),],  max_length=200, default="")
    
    p9=models.CharField(verbose_name="Você toma medicação para alguma doença cronica?", choices=[('sim', 'SIM'), ('não', 'NÃO')],  max_length=200, default="")
    
    p10=models.CharField(verbose_name="Você já teve um derrame? ", choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=200, default="")

    p11=models.CharField(verbose_name="Você ja teve um coágulo sangüíneo em seus pulmões?", choices=[('SIM (JÁ TIVE)', 'SIM (JÁ TIVE)'), ('NÃO (NUNCA TIVE)', 'NÃO (NUNCA TIVE)')],  max_length=200, default="")
    p12=models.CharField(verbose_name="Você ja teve um coágulo sangüíneo em seuas pernas", choices=[('SIM (JÁ TIVE)', 'SIM (JÁ TIVE)'), ('NÃO (NUNCA TIVE)', 'NÃO (NUNCA TIVE)')],  max_length=200, default="")
    #perguntas relativa a pilula só de Progestógeno
    p13=models.CharField(verbose_name="Você tem  câncer de mama?" , choices=[('TENHO', 'TENHO'), ('SIM (JÁ TIVE)', 'SIM (JÁ TIVE)'), ('NÃO (NUNCA TIVE)', 'NÃO (NUNCA TIVE)')],  max_length=200, default="")
    p14=models.CharField(verbose_name="Você tem sangramento vaginal?" , choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')],  max_length=200, default="")
    similaridade=models.FloatField(default=0, verbose_name='RESULTADO')

    def resultado(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        if(self.p1=="SIM"):
            self.p1=100
        elif(self.p1=="NÃO"):
            self.p1=0
        else:
            self.p1=0

        if(self.p2=="SIM"):
            self.p2=100
        elif(self.p2=="NÃO"):
            self.p2=0
        else:
            self.p2=0

        if(self.p3=="SIM FUMO (1 há 5)"):
            self.p3=25
        elif(self.p3=="SIM FUMO (5 há 10)"):
            self.p3=500          
        elif(self.p3=="SIM FUMO (10 há 20)"):
            self.p3=100
        elif(self.p3=="NÃO, NÃO FUMO"):
            self.p3=0 
        else:
            self.p3=0

        if(self.p4=="SIM"):
            self.p4=100
        elif(self.p4=="NÃO"):
            self.p4=0           
        elif(self.p4=="NÃO SEI"):
            self.p4=25
        elif(self.p4=="TALVEZ"):
            self.p4=50 
        else:
            self.p4=0

        if(self.p5=="SIM"):
            self.p5=100
        elif(self.p5=="NÃO"):
            self.p5=0           
        elif(self.p5=="NÃO SEI"):
            self.p5=25
        elif(self.p5=="TALVEZ"):
            self.p5=50 
        else:
            self.p5=0

        if(self.p6=="SIM (TENHO PRESSÃO ALTA)"):
            self.p6=100
        elif(self.p6=="SIM (TENHO PRESSÃO BAIXA)"):
            self.p6=100       
        elif(self.p6=="NÃO (NÃO TENHO)"):
            self.p6=0
        elif(self.p6=="NÃO SEI"):
            self.p6=25
        else:
            self.p6=0

        if(self.p7=="SIM TENHO"):
            self.p7=100
        elif(self.p7=="NÃO TENHO"):
            self.p7=0           
        elif(self.p7=="JÁ TIVE"):
            self.p7=25
        else:
            self.p7=0
       
        if(self.p8=="SIM"):
            self.p8=100
        elif(self.p8=="NÃO"):
            self.p8=0
        else:
            self.p8=0

        if(self.p9=="SIM"):
            self.p9=100
        elif(self.p9=="NÃO"):
            self.p9=0
        else:
            self.p9=0

        if(self.p10=="SIM"):
            self.p10=100
        elif(self.p10=="NÃO"):
            self.p10=0
        else:
            self.p10=0


        if(self.p11=="SIM (JÁ TIVE)"):
            self.p11=100
        elif(self.p11=="NÃO (NUNCA TIVE)"):
            self.p11=0
        else:
            self.p11=0

        if(self.p12=="SIM (JÁ TIVE)"):
            self.p12=100
        elif(self.p12=="NÃO (NUNCA TIVE)"):
            self.p12=0
        else:
            self.p12=0

        if(self.p13=="TENHO"):
            self.p13=100
        elif(self.p13=="SIM (JÁ TIVE)"):
            self.p13=50          
        elif(self.p13=="NÃO (NUNCA TIVE)"):
            self.p13=0
        else:
            self.p13=0
        
        if(self.p14=="SIM"):
            self.p14=100
        elif(self.p14=="NÃO"):
            self.p14=0
        else:
            self.p14=0
        
        self.similaridade=math.sqrt(
            (10*(self.p1-p1)**2)+
            (10*(self.p2-p2)**2)+
            (5*(self.p3-p3)**2)+
            (10*(self.p4-p4)**2)+
            (7*(self.p5-p5)**2)+
            (10*(self.p6-p6)**2)+
            (9*(self.p7-p7)**2)+
            (5*(self.p8-p8)**2)+
            (10*(self.p9-p9)**2)+
            (6*(self.p10-p10)**2)+
            (10*(self.p11-p11)**2)+
            (10*(self.p12-p12)**2)+
            (4*(self.p13-p13)**2)+
            (10*(self.p14-p14)**2)
            )

        return "%1.2f"%self.similaridade 
