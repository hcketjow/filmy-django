from django.urls import path
# from .views import SearchResultsView
from filmyweb.views import wszystkie_filmy, nowy_film, edytuj_film, usun_film,lista_film

urlpatterns = [
    path('wszystkie/', wszystkie_filmy, name="wszystkie_filmy"),
    path('nowy/', nowy_film, name="nowy_film"),
    path('edytuj/<int:id>/', edytuj_film, name="edytuj_film"),
    path('usun/<int:id>/', usun_film, name="usun_film"),
    path('lista/', lista_film, name="lista_film"),
    # path('search/', SearchResultsView.as_view(), name='search_results'),
]
