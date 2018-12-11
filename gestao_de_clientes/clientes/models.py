from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    age = models.IntegerField()
    salario = models.DecimalField(max_digits=7, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clientes_photos', null=True, blank=True)

    def __str__(self):
        return self.nome