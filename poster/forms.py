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
