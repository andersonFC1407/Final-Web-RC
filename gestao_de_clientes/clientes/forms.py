from django.forms import ModelForm
from .models import Pessoa

class PersonForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'sobrenome', 'age', 'salario', 'bio','photo']