from django.contrib import admin
from .models import PerguntaFrequente

@admin.register(PerguntaFrequente)
class PerguntaFrequenteAdmin(admin.ModelAdmin):
    list_display =(
        'pergunta',
        'ativa',
        'ordem'
    )
    
    list_filter = (
        'ativa',
    )
    
    search_fields = (
        'pergunta',
        'resposta'
    )
    
    