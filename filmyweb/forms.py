from django.db.models import fields
from django.db.models.fields import files
from django.forms import ModelForm
from .models import Film, DodatkoweInfo, Ocena

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'opis', 'rok', 'imdb_rating', 'plakat','rezyseria','scenaruisz','produkcja']

class DodatkoweInfoForm(ModelForm):
    class Meta:
        model = DodatkoweInfo
        fields = ['czas_trwania', 'gatunek']

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['gwiazdki', 'recenzja']
