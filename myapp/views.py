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
            id = w.get_id()
            data = w.readRep(id)
            if 'SearchedWith' in data:
                searchedWithCaption = "Searched with " + "'" + w.phrase + "'"
                searchedWithData = data["SearchedWith"]
                thListW = ["Phrase", "Shows"]
            else:
                thListW = []
            if 'SearchedAlso' in data:
                searchedAlsoCaption = "Searched like " + "'" + w.phrase + "'"
                searchedAlsoData = data["SearchedAlso"]
                thListA = ["Phrase", "Shows"]
            else:
                thListA =[]
        args = {'form': form, 'data': data, 'searchedWithCaption': searchedWithCaption, 'searchedAlsoCaption': searchedAlsoCaption, 'searchedWithData': searchedWithData, 'searchedAlsoData': searchedAlsoData, 'thListW': thListW, 'thListA': thListA}
        return render(request, self.template_name, args)