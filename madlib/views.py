from django.shortcuts import render
from .form import MadlibForm
from random import randint


# Create your views here.
def home(request):
    return render(request, 'madlib/welcome.html')


def madlib_form(request):
    form = MadlibForm(request.POST or None)
    context = {'form': form,
               'navbar': 'yes'}
    value = randint(1, 15)
    pic = ['hal', 'mountain', 'fishing', 'hal', 'hal', 'hal', 'hal', 'mountain', 'mountain',
           'mountain', 'mountain', 'fishing', 'fishing', 'fishing', 'fishing']
    index = value - 1
    id_pic = pic[index]

    if form.is_valid():
        context = {'adj': form.cleaned_data.get('adjective'),
                   'adj2': form.cleaned_data.get('adjective2'),
                   'place': form.cleaned_data.get('place'),
                   'verb': form.cleaned_data.get('verb'),
                   'animal': form.cleaned_data.get('animal'),
                   'adverb': form.cleaned_data.get('adverb'),
                   'name': form.cleaned_data.get('name'),
                   'message': 'yes',
                   'navbar': 'yes',
                   'id_pic': id_pic}
        path = f'madlib/story/story{value}.html'
        return render(request, path, context)

    return render(request, 'madlib/form.html', context)
