from django import forms
from bapi_scrape.scripts.courses.scrape import get_dropdown_choices

def format_choices(choices):
    l = []
    for k, v in choices.items():
      l.append((v, k))

    return l

class CourseCategoriesForm(forms.Form):
    choice = forms.ChoiceField(choices=format_choices(get_dropdown_choices()))