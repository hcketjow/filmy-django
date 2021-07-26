from django.db import models

class DodatkoweInfo(models.Model):
    GATUNEK = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Drama'),
        (5, 'Akcja'),
        (6, 'Przygodowy'),
    }

    czas_trwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)

class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True) 
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default="", max_length=1000)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,null=True, blank=True)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)
    rezyseria = models.CharField(default="", max_length=100)
    scenaruisz = models.CharField(default="", max_length=100)
    produkcja = models.CharField(default="", max_length=100)
    

    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)

class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film, related_name="aktorzy")

