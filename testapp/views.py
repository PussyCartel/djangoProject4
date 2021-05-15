from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import LoadForm
from .models import *


class BaseView(TemplateView):
    template_name = 'base.html'


class ThanksView(TemplateView):
    template_name = 'thanks.html'


def questions(request):
    if request.method == 'POST':
        form = LoadForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = LoadForm()
    return render(request, 'form.html', {'form': form})
