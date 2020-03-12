from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

REGIONS = (
    ('D', 'dolnośląskie'),
    ('C', 'kujawsko-pomorskie'),
    ('L', 'lubelskie'),
    ('F', 'lubuskie'),
    ('E', 'łódzkie'),
    ('K', 'małopolskie'),
    ('W', 'mazowieckie'),
    ('O', 'opolskie'),
    ('R', 'podkarpackie'),
    ('B', 'podlaskie'),
    ('G', 'pomorskie'),
    ('S', 'śląskie'),
    ('T', 'świętokrzyskie'),
    ('N', 'warmińsko-mazurskie'),
    ('P', 'wielkopolskie'),
    ('Z', 'zachodniopomorskie'),
)


# Create your models here.

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_prim = models.CharField(max_length=32,
                                  verbose_name=_("Phone number"),
                                  help_text=_("Enter primary phone number"))
    phone_second = models.CharField(max_length=32, null=True,
                                    verbose_name=_("Phone number additional"),
                                    help_text=_("Enter secondary/additional phone number"))
    country = models.TextField(max_length=32, default=_('Poland'))
    region = models.CharField(max_length=1, choices=REGIONS,
                              verbose_name=_("Region"),
                              help_text=_("Choose region"))
    city = models.TextField(max_length=64,
                            verbose_name=_("City"),
                            help_text=_("Enter city"))
    zip_code = models.TextField(max_length=8,
                                verbose_name=_("ZIP code"),
                                help_text=_("Enter ZIP code"))
    street = models.TextField(max_length=64, null=True)


class FileType(models.Model):
    type = models.CharField(max_length=16, default='')


class Photo(models.Model):
    title = models.CharField(max_length=32, default='',
                             verbose_name=_("Short name"),
                             help_text=_("Enter short photo name"))
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
    #                          verbose_name=_("User"),
    #                          help_text=_("Choose photo owner"))
    description = models.TextField(max_length=64, null=True,
                                   verbose_name=_("Description"),
                                   help_text=_("Fill photo description"))
    taken_localisation = models.CharField(max_length=64, null=True,
                                          verbose_name=_("Photo taken location"),
                                          help_text=_("Enter photo taken location"))
    taken_datetime = models.DateTimeField(null=True,
                                          verbose_name=_("Date, time photo taken"),
                                          help_text=_("Enter date and time of photo taken"))
    file_name_origin = models.CharField(max_length=64, default='')
    file_name_hashed = models.CharField(max_length=64, default='')
    path_loaded = models.CharField(max_length=256, default='')
    file_type = models.ForeignKey(FileType, on_delete=models.SET(None), default=None)
    update_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=32, default='',
                            verbose_name=_("Name"),
                            help_text=_("Enter name category"))
    icon_name = models.CharField(max_length=64, default='',
                                 verbose_name=_("Icon"),
                                 help_text=_("Enter icon file name"))
    active = models.BooleanField(default=True,
                                 verbose_name=_("Active"),
                                 help_text=_("Marked if catagery is active"))
    update_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)


class SalePoster(models.Model):
    title = models.CharField(max_length=64,
                             verbose_name=_("Short name"),
                             help_text=_("Enter short sale name"))
    categories = models.ManyToManyField(Category, null=True,
                                        verbose_name=_("Categories"),
                                        help_text=_("You can choose many categories"))
    total_value = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name=_("Total value"),
                                      help_text=_("Enter total value"))
    photos = models.ManyToManyField(Photo, null=True,
                                    verbose_name=_("Photos"),
                                    help_text=_("You can choose many photos"))
    description = models.TextField(max_length=512, null=True,
                                   verbose_name=_("Description"),
                                   help_text=_("Fill photo description"))
    country = models.TextField(max_length=32, default=_('Poland'))
    city = models.TextField(max_length=64,
                            verbose_name=_("City"),
                            help_text=_("Enter city"))
    region = models.CharField(max_length=1, choices=REGIONS,
                              verbose_name=_("Region"),
                              help_text=_("Choose region"))
    zip_code = models.TextField(max_length=8,
                                verbose_name=_("ZIP code"),
                                help_text=_("Enter ZIP code"))
    street = models.TextField(max_length=64, null=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    active = models.BooleanField(default=True)
    # end_date = models.DateTimeField(default=datetime.now(locals()) + 10 days)
    update_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)
