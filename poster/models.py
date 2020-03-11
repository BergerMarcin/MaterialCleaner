from django.contrib.auth.models import User
from django.db import models

REGIONS = (
    ('D', 'dolnośląskie'),
    ('C', 'kujawsko-pomorskie'),
    ('L', 'lubelskie'),
    ('F', 'lubuskie'),
    ('E', 'łódzkie'),
    ('K', 'małopolskie'),
    ('W', 'mazowieckie'),
    ('O', 'opolskie'),
    ('R', 'podkarpacke'),
    ('B', 'podlaskie'),
    ('G', 'pomorskie'),
    ('S', 'śląskie'),
    ('T', 'świętokrzskie'),
    ('N', 'warmińsko-mazursie'),
    ('P', 'wielkopolskie'),
    ('Z', 'zachodniopomorsie'),
)


# Create your models here.

class FileType(models.Model):
    type = models.CharField(max_length=16, default='')


class Photo(models.Model):
    title = models.CharField(max_length=32, default='',
                             verbose_name="Krótka nazwa",
                             help_text="Podaj krótką nazwę zdjęcia")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                             verbose_name="Użytkownik",
                             help_text="Wybierz właściciela zdjęcia")
    description = models.TextField(max_length=256, null=True,
                                   verbose_name="Opis",
                                   help_text="Podaj opis zdjęcia")
    taken_localisation = models.CharField(max_length=64, null=True,
                                          verbose_name="Miejsce wykonania",
                                          help_text="Podaj miejsce wykonania zdjęcia")
    taken_datetime = models.DateTimeField(null=True,
                                          verbose_name="Data, godzina wykonania",
                                          help_text="Podaj datę, godzinę wykonania zdjęcia")
    file_name_original = models.CharField(max_length=64, default='')
    file_name_hashed = models.CharField(max_length=64, default='')
    pathname_hashed = models.CharField(max_length=256, default='')
    file_type = models.ForeignKey(FileType, on_delete=models.SET(None), default=None)
    update_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=32, default='',
                            verbose_name="Nazwa",
                            help_text="Podaj nazwę kategorii")
    icon_name = models.CharField(max_length=64, default='',
                                 verbose_name="Nazwa pliku",
                                 help_text="Podaj nazwę pliku ikonki")
    active = models.BooleanField(default=True,
                                 verbose_name="Aktywna",
                                 help_text="Zaznacz jeżeli kategoria jest aktywna")
    update_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)


class Sale(models.Model):
    title = models.CharField(max_length=64,
                             verbose_name="Krótka nazwa",
                             help_text="Podaj krótką nazwę zdjęcia")
    categories = models.ManyToManyField(Category,
                                        verbose_name="Kategorie",
                                        help_text="Możesz wybrać wiele kategorii")
    total_value = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name="Wartość",
                                      help_text="Podaj wartość całkowitą")
    photos = models.ManyToManyField(Photo,
                                    verbose_name="Zdjęcia",
                                    help_text="Możesz wybrać wiele zdjęć z Twojego dysku")
    description = models.TextField(max_length=512, null=True,
                                   verbose_name="Opis",
                                   help_text="Podaj opis")
    country = models.TextField(max_length=32, default='Polska')
    city = models.TextField(max_length=64,
                            verbose_name="Miasto",
                                    help_text="Podaj miasto")
    region = models.CharField(max_length=1, choices=REGIONS,
                              verbose_name="Wojwództwo",
                              help_text="Wybierz województwo")
    zip_code = models.TextField(max_length=8,
                                verbose_name="Kod pocztowy",
                                help_text="Podaj kod pocztowy")
    street = models.TextField(max_length=64, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    active = models.BooleanField(default=True)
    # end_date = models.DateTimeField(default=datetime.now(locals()) + 10 days)
    update_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)
