from django.db import models

# Create your models here.
class PerguntaFrequente(models.Model):
    pergunta = models.CharField(
        max_length=255
    )
    
    resposta = models.TextField()
    
    ordem = models.PositiveIntegerField(
        default=0
    )
    
    ativa = models.BooleanField(
        default=True
    )
    
    criada_em = models.DateTimeField(
        auto_now_add=True
    )
    
    class Meta:
        ordering = ['ordem', 'pergunta']
        
    def __str__(self):
        return self.pergunta