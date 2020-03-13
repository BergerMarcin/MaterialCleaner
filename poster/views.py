from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import FormView
from django.utils import translation
from materialcleaner.settings import LANGUAGES, LANGUAGE_CODE
from .models import UserDetail
from .uploaded_files_operations import handle_uploaded_photo_files
from .forms import LanguageForm, LoginForm, PhotoUploadForm, UserAddForm


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
        ctx = {'form_lang': form_lang}
        return render(request, 'index.html', ctx)
    
    def post(self, request):
        request = change_language(request)
        return redirect("/index")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        form_lang = LanguageForm()
        ctx = {'form': form, 'form_lang': form_lang}
        return render(request, 'login.html', ctx)
    
    def post(self, request):
        request = change_language(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['identifier'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect("/index")
        form_lang = LanguageForm()
        ctx = {'form': form, 'form_lang': form_lang}
        return render(request, 'login.html', ctx)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/index")


class UserAddView(View):
    def get(self, request):
        form = UserAddForm()
        form_lang = LanguageForm()
        ctx = {'form': form, 'form_lang': form_lang}
        return render(request, 'user_add.html', ctx)
    
    def post(self, request):
        request = change_language(request)
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                is_superuser=False,
                is_staff=False,
                is_active=True,
            )
            regular = Group.objects.get(name='regular')
            user.groups.add(regular)
            user.save()
            user_detail = UserDetail.objects.create(
                user=user,
                phone_prim=form.cleaned_data['phone_prim'],
                phone_second=form.cleaned_data['phone_second'],
                country=form.cleaned_data['country'],
                region=form.cleaned_data['region'],
                city=form.cleaned_data['city'],
                zip_code=form.cleaned_data['zip_code'],
            )
            return redirect("/login")
        form_lang = LanguageForm()
        ctx = {'form': form, 'form_lang': form_lang}
        return render(request, 'user_add.html', ctx)


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    def get(self, request):
        user = request.user
        userdetail = UserDetail.objects.get(user=user)
        form = UserAddForm()
        form.username = user.username
        form.first_name = user.first_name
        form.last_name = user.last_name
        form.email = user.email
        form.phone_prim = userdetail.phone_prim
        form.phone_second = userdetail.phone_second
        form.country = userdetail.country
        form.region = userdetail.region
        form.city = userdetail.city
        form.zip_code = userdetail.zip_code
        form.street = userdetail.street
        form_lang = LanguageForm()
        ctx = {'form': form, 'form_lang': form_lang}
        return render(request, 'user_update.html', ctx)
    
    def post(self, request):
        request = change_language(request)
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                is_superuser=False,
                is_staff=False,
                is_active=True,
            )
            regular = Group.objects.get(name='regular')
            user.groups.add(regular)
            user.save()
            user_detail = UserDetail.objects.create(
                user=user,
                phone_prim=form.cleaned_data['phone_prim'],
                phone_second=form.cleaned_data['phone_second'],
                country=form.cleaned_data['country'],
                region=form.cleaned_data['region'],
                city=form.cleaned_data['city'],
                zip_code=form.cleaned_data['zip_code'],
            )
            return redirect("/login")
        form_lang = LanguageForm()
        ctx = {'form': form, 'form_lang': form_lang}
        return render(request, 'user_update.html', ctx)


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
