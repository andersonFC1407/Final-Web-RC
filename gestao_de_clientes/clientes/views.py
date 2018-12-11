from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pessoa
from .forms import PersonForm


# Create your views here.
@login_required
def persons_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'person.html', {"pessoas": pessoas})

@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

@login_required
def persons_update(request, pk):
    data={}
    pessoa = get_object_or_404(Pessoa, pk=pk)
    form = PersonForm(request.POST or None, request.FILES or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    data['form'] = form
    data['pessoa'] = pessoa
    return render(request, 'person_form.html', {'form':form})

@login_required
def persons_delete(request, pk):
    person = get_object_or_404(Pessoa, pk=pk)
    form = PersonForm(instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'pessoa': person})