from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import FormView
from django.utils import translation
from materialcleaner.settings import LANGUAGES, LANGUAGE_CODE
from .uploaded_files_operations import handle_uploaded_photo_files
from .forms import LanguageForm, LoginForm, PhotoUploadForm


# Create your views here.

# TODO: after each change User or UserDetails and Login checking user if
#  user belongs to proper UserGroup (regular / inactive_regular) acc. active status

def change_language(request):
    form_lang = LanguageForm(request.POST)
    if form_lang.is_valid():
        lang = form_lang.cleaned_data['language']
        if lang in list(lang[0] for lang in LANGUAGES):
            translation.activate(lang)
            request.session[translation.LANGUAGE_SESSION_KEY] = lang
    return request


class IndexBaseWithLanguageChoiceView(View):
    '''
    Index View = Base View with language form choice at template base.html
    Redirected to index url_name
    '''
    
    def get(self, request):
        form_lang = LanguageForm()
        return render(request, 'index.html', {'form': form_lang})
    
    def post(self, request):
        request = change_language(request)
        return redirect("/index")


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request):
        request = change_language(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
        return redirect("/index")


# -----------------------------------------------

class PhotoListView(View):
    def get(self, request):
        return TemplateResponse(request, "index.html")


class PhotoUploadView(FormView):
    '''
    Upload files
    https://docs.djangoproject.com/en/2.2/topics/http/file-uploads/#uploading-multiple-files
    '''
    form_class = PhotoUploadForm
    template_name = 'upload.html'
    success_url = '/'
    
    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for i, file in enumerate(files):
                files_written = handle_uploaded_photo_files(file)
                if files_written:
                    # TODO: save file_hashed to the base
                    # photo = Photo(title = form.cleaned_data['title'] + '_' + str(i),
                    #               user = User.username,
                    #               description='',
                    #               taken_localisation='',
                    #               file_name_hashed=files_written['file_name_hashed'],
                    #               path_loaded=files_written['path_loaded'],
                    #               file_type=files_written['file_type'])
                    # print(photo)
                    # photo.save()
                    pass
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
