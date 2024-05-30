from django.db import models

class Topic(models.Model):
    """""Um assunto sobre o nqual o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """"Devolve uma representação em string don modelo"""
        return self.text

