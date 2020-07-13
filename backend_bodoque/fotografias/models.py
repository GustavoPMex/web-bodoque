from django.db import models

# Create your models here.

class Fotografia(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    image = models.ImageField(upload_to='fotografia', verbose_name='Imagen')
    description = models.CharField(max_length=200, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Fotografia'
        verbose_name_plural = 'Fotografias'
        ordering = ['created']
        