from django.contrib import admin
from core.models import *

class PerguntaInlne(admin.TabularInline):
    model=Pergunta
    extra=0


class AntiAdmin(admin.ModelAdmin):
    inlines=[PerguntaInlne]
    ordering = ['name']
    search_fields = ['name']
    save_as=True
    save_on_top=True

class RespostaInlne(admin.TabularInline):
    model=Resposta
    extra=1
    max_num=1

class RegrasAdmin(admin.ModelAdmin):
    inlines=[RespostaInlne]
    list_display=('__str__','anti','pergunta', 'regra')
    list_display_links=('anti', 'regra')
    #ordering = ['-id']
    search_fields = ['resposta']
    save_as=True

class AntiInlne(admin.TabularInline):
    model=Anti
    extra=0


class CategooriaAdmin(admin.ModelAdmin):
    inlines=[AntiInlne]
    ordering = ['category']
    search_fields = ['category']
    save_as=True

class PerguntaAdmin(admin.ModelAdmin):
    list_display=('similaridade','total','p1','p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26')
    list_display_links=('similaridade','p1','p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26')

    #list_display_links=('anti', 'regra')
    #ordering = ['-id']
    search_fields = ['p1']
    save_as=True
    save_on_top=True
    



admin.site.register(Category, CategooriaAdmin)
admin.site.register(Anti, AntiAdmin)
admin.site.register(Regra, RegrasAdmin)

admin.site.register(Pergunta, PerguntaAdmin)




