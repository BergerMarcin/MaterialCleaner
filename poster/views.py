from django.shortcuts import render, redirect
from django.views import View
from django.utils import translation
from materialcleaner.settings import LANGUAGES, LANGUAGE_CODE
from .forms import BaseForm


# Create your views here.

class IndexBaseWithLanguageChoiceView(View):
    '''
    Index View = Base View with language form choice at template base.html
    Redirected to index url_name
    '''
    
    def get(self, request):
        form = BaseForm()
        return render(request, 'base-language.html', {'form': form})
    
    def post(self, request):
        form = BaseForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            if language in list(lang[0] for lang in LANGUAGES):
                translation.activate(language)
                request.session[translation.LANGUAGE_SESSION_KEY] = language
        return redirect("/index")
