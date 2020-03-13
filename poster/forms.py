from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from materialcleaner.settings import LANGUAGES, REGIONS
from django.utils.translation import ugettext_lazy as _

from poster.models import UserDetail


# Validation: unique username @ DB (add, update user)
def validate_username_unique(value):
    if User.objects.filter(username=value).count() > 0:
        raise ValidationError(_('Username already exists. Please write another username'))

# Validation: existing username @ DB (login)
def validate_username_exist(value):
    if User.objects.filter(username=value).count() == 0:
        raise ValidationError(_('Unknown username. Please write another username'))

# Validation: unique email @ DB (add, update user)
def validate_email_unique(value):
    if User.objects.filter(email=value).count() > 0:
        raise ValidationError(_('Email already exists. Please write another email'))

# Validation: existing email @ DB (login)
def validate_email_exist(value):
    if User.objects.filter(email=value).count() == 0:
        raise ValidationError(_('Unknown email. Please write another email'))

# Validation: unique primary phone @ DB (add, update user)
def validate_phone_prim_unique(value):
    if UserDetail.objects.filter(phone_prim=value).count() > 0:
        raise ValidationError(_('Phone number (primary) already exists. Please write another phone number'))

# Validation: existing primary phone @ DB (login)
def validate_phone_prim_exist(value):
    if UserDetail.objects.filter(phone_prim=value).count() == 0:
        raise ValidationError(_('Unknown phone number (primary). Please write another phone number'))


class LanguageForm(forms.Form):
    language = forms.ChoiceField(choices=LANGUAGES,
                                 label=_('Language'), help_text=_('Choose language'))


class PhotoUploadForm(forms.Form):
    title = forms.CharField(max_length=256,
                            label=_('Common photo name'), help_text=_('Fill-in common name for all photos'))
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),
                            label=_('Photos'), help_text=_('Choose photos'))


class LoginForm(forms.Form):
    identifier = forms.CharField(label=_('Username / email / primary phone number'),
                                 min_length=3, max_length=64,
                                 validators=[validate_username_exist,
                                             # validate_email_exist,
                                             # validate_phone_prim_exist
                                             ],
                                 required=True)
    password = forms.CharField(label=_('Password'), max_length=16, widget=forms.PasswordInput, required=True)
    re_password = forms.CharField(label=_('Repeat password'), max_length=16, widget=forms.PasswordInput, required=True)
    
    # Validation re_password
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError(_('Password was repeated wrongly'))


class UserAddForm(forms.Form):
    username = forms.CharField(label=_('Username'), min_length=3, max_length=64,
                               validators=[validate_username_unique], required=True)
    first_name = forms.CharField(label=_('First name'), min_length=3, max_length=64, required=True)
    last_name = forms.CharField(label=_('Last name'), min_length=3, max_length=64, required=True)
    email = forms.CharField(label=_('Email'), validators=[EmailValidator(), validate_email_unique], required=True)
    phone_prim = forms.CharField(label=_('Phone number'), min_length=9, max_length=32,
                                 validators=[validate_phone_prim_unique], required=True)
    phone_second = forms.CharField(label=_('Phone number additional'), max_length=32)
    country = forms.CharField(label=_('Country'), max_length=32, required=True)
    region = forms.ChoiceField(label=_('Choose region'), choices=REGIONS, required=True)
    city = forms.CharField(label=_('City'), min_length=3, max_length=32, required=True)
    zip_code = forms.CharField(label=_('ZIP code'), min_length=3, max_length=8, required=True)
    street = forms.CharField(label=_('Street, house and flat no.'), max_length=64)
    password = forms.CharField(label=_('Password'), max_length=16, widget=forms.PasswordInput, required=True)
    re_password = forms.CharField(label=_('Repeat password'), max_length=16, widget=forms.PasswordInput, required=True)
    
    # Validation re_password
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError(_('Password was repeated wrongly'))


class UserAddForm(forms.Form):
    username = forms.CharField(label=_('Username'), min_length=3, max_length=64,
                               validators=[validate_username_unique], required=True)
    first_name = forms.CharField(label=_('First name'), min_length=3, max_length=64, required=True)
    last_name = forms.CharField(label=_('Last name'), min_length=3, max_length=64, required=True)
    email = forms.CharField(label=_('Email'), validators=[EmailValidator(), validate_email_unique], required=True)
    phone_prim = forms.CharField(label=_('Phone number'), min_length=9, max_length=32,
                                 validators=[validate_phone_prim_unique], required=True)
    phone_second = forms.CharField(label=_('Phone number additional'), max_length=32)
    country = forms.CharField(label=_('Country'), max_length=32, required=True)
    region = forms.ChoiceField(label=_('Choose region'), choices=REGIONS, required=True)
    city = forms.CharField(label=_('City'), min_length=3, max_length=32, required=True)
    zip_code = forms.CharField(label=_('ZIP code'), min_length=3, max_length=8, required=True)
    street = forms.CharField(label=_('Street, house and flat no.'), max_length=64)
    password = forms.CharField(label=_('Password'), max_length=16, widget=forms.PasswordInput, required=True)
    re_password = forms.CharField(label=_('Repeat password'), max_length=16, widget=forms.PasswordInput, required=True)
    
    # Validation re_password
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError(_('Password was repeated wrongly'))


class UserUpdateForm(forms.Form):
    username = forms.CharField(label=_('Username'), min_length=3, max_length=64,
                               validators=[validate_username_unique], required=True)
    first_name = forms.CharField(label=_('First name'), min_length=3, max_length=64, required=True)
    last_name = forms.CharField(label=_('Last name'), min_length=3, max_length=64, required=True)
    email = forms.CharField(label=_('Email'), validators=[EmailValidator(), validate_email_unique], required=True)
    phone_prim = forms.CharField(label=_('Phone number'), min_length=9, max_length=32,
                                 validators=[validate_phone_prim_unique], required=True)
    phone_second = forms.CharField(label=_('Phone number additional'), max_length=32)
    country = forms.CharField(label=_('Country'), max_length=32, required=True)
    region = forms.ChoiceField(label=_('Choose region'), choices=REGIONS, required=True)
    city = forms.CharField(label=_('City'), min_length=3, max_length=32, required=True)
    zip_code = forms.CharField(label=_('ZIP code'), min_length=3, max_length=8, required=True)
    street = forms.CharField(label=_('Street, house and flat no.'), max_length=64)
    password = forms.CharField(label=_('Password'), max_length=16, widget=forms.PasswordInput, required=True)
    re_password = forms.CharField(label=_('Repeat password'), max_length=16, widget=forms.PasswordInput, required=True)
    
    # Validation re_password
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError(_('Password was repeated wrongly'))


class UserResetPasswordForm(forms.Form):
    password = forms.CharField(label=_('Password'), max_length=16, widget=forms.PasswordInput, required=True)
    re_password = forms.CharField(label=_('Repeat password'), max_length=16, widget=forms.PasswordInput, required=True)
    
    # Validation re_password
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('Błędnie powtórzone hasło!')

# Day3 2_Uprawnienia Task1
# class UserListView(PermissionRequiredMixin, View):
#     permission_required = 'auth.change_user'
