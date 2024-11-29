from django.contrib import admin
from .models import Pergunta, Resposta

class RespostaInline(admin.StackedInline):
    model = Resposta
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]
    fields = ['data_pub','texto_da_pergunta']

admin.site.register(Pergunta, PerguntaAdmin)
#admin.site.register(Resposta)
