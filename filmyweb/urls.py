from django.contrib.auth import views
from django.urls import path
# from .views import SearchResultsView
from filmyweb.views import wszystkie_filmy, nowy_film, edytuj_film, usun_film,lista_film,export_excel,export_xml

urlpatterns = [
    # wszystkie/
    path('', wszystkie_filmy, name="wszystkie_filmy"),
    path('nowy/', nowy_film, name="nowy_film"),
    path('edytuj/<int:id>/', edytuj_film, name="edytuj_film"),
    path('usun/<int:id>/', usun_film, name="usun_film"),
    path('lista/', lista_film, name="lista_film"),
    path('export_excel', export_excel, name='export_excel'),
    path('export_xml', export_xml, name='export_xml')
    # path('search/', SearchResultsView.as_view(), name='search_results'),
]
