from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import FormView
from django.utils import translation
from materialcleaner.settings import LANGUAGES, LANGUAGE_CODE
from .uploaded_files_operations import handle_uploaded_photo_files
from .forms import BaseForm, PhotoUploadForm


# Create your views here.

# TODO: after each change User or UserDetails and Login checking user if
#  user belongs to proper UserGroup (regular / inactive_regular) acc. active status


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
