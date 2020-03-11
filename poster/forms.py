from django import forms
from materialcleaner.settings import LANGUAGES
from django.utils.translation import ugettext_lazy as _


class BaseForm(forms.Form):
    '''
    Base form
    !!! OTHER FORMS should EXTENDS thar FORM (to have language field) !!! ;)
    '''
    language = forms.ChoiceField(choices=LANGUAGES,
                                 label=_('Language'), help_text=_('Choose language'))


class PhotoUploadForm(BaseForm):
    title = forms.CharField(max_length=256,
                            label='Zbiorcza nazwa zdjęć', help_text='Podaj zbiorczą nazwę pobieranych zdjęć')
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),
                           label='Zdjęcia', help_text='Wskaż lokalizację zdjęć')
