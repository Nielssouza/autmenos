from django.shortcuts import render
from .models import PerguntaFrequente

# Create your views here.
def central_ajuda(request):
    perguntas = PerguntaFrequente.objects.filter(
        ativa=True
    )
    
    return render(
        request,
        'ajuda/central_ajuda.html',
        {
            'perguntas': perguntas
        }
    )