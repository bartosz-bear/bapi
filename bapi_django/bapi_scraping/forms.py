from django import forms
from bapi_scraping.scripts.coursera_scraper import get_dropdown_choices

def format_choices(choices):
    l = []
    for k, v in choices.items():
      l.append((v, k))
    print(l)

    return l

class NameForm(forms.Form):
    choice = forms.ChoiceField(choices=format_choices(get_dropdown_choices()))


