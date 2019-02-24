from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView
from .forms import WordForm
from .models import WordStat


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = WordForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = WordForm(request.POST)
        if form.is_valid():
            w = WordStat(form.cleaned_data['word'])
            text = w.get_id()
            #text = form.cleaned_data['word']
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)