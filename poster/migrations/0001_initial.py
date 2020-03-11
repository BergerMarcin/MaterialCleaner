# Generated by Django 2.2.10 on 2020-03-11 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_prim', models.CharField(help_text='Enter primary phone number', max_length=32, verbose_name='Phone number')),
                ('phone_second', models.CharField(help_text='Enter secondary/additional phone number', max_length=32, verbose_name='Phone number additional')),
                ('country', models.TextField(default='Poland', max_length=32)),
                ('city', models.TextField(help_text='Enter city', max_length=64, verbose_name='City')),
                ('region', models.CharField(choices=[('D', 'dolnośląskie'), ('C', 'kujawsko-pomorskie'), ('L', 'lubelskie'), ('F', 'lubuskie'), ('E', 'łódzkie'), ('K', 'małopolskie'), ('W', 'mazowieckie'), ('O', 'opolskie'), ('R', 'podkarpacke'), ('B', 'podlaskie'), ('G', 'pomorskie'), ('S', 'śląskie'), ('T', 'świętokrzskie'), ('N', 'warmińsko-mazursie'), ('P', 'wielkopolskie'), ('Z', 'zachodniopomorsie')], help_text='Choose region', max_length=1, verbose_name='Region')),
                ('zip_code', models.TextField(help_text='Enter ZIP code', max_length=8, verbose_name='ZIP code')),
                ('street', models.TextField(max_length=64, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Enter name category', max_length=32, verbose_name='Name')),
                ('icon_name', models.CharField(default='', help_text='Enter icon file name', max_length=64, verbose_name='Icon')),
                ('active', models.BooleanField(default=True, help_text='Marked if catagery is active', verbose_name='Active')),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', help_text='Enter short photo name', max_length=32, verbose_name='Short name')),
                ('description', models.TextField(help_text='Fill photo description', max_length=256, null=True, verbose_name='Description')),
                ('taken_localisation', models.CharField(help_text='Enter photo taken location', max_length=64, null=True, verbose_name='Photo taken location')),
                ('taken_datetime', models.DateTimeField(help_text='Enter date and time of photo taken', null=True, verbose_name='Date, time photo taken')),
                ('file_name_original', models.CharField(default='', max_length=64)),
                ('file_name_hashed', models.CharField(default='', max_length=64)),
                ('pathname_hashed', models.CharField(default='', max_length=256)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('file_type', models.ForeignKey(default=None, on_delete=models.SET(None), to='poster.FileType')),
                ('user', models.ForeignKey(help_text='Choose photo owner', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='SalePoster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter short sale name', max_length=64, verbose_name='Short name')),
                ('total_value', models.DecimalField(decimal_places=2, help_text='Enter total value', max_digits=10, verbose_name='Total value')),
                ('description', models.TextField(help_text='Fill photo description', max_length=512, null=True, verbose_name='Description')),
                ('country', models.TextField(default='Poland', max_length=32)),
                ('city', models.TextField(help_text='Enter city', max_length=64, verbose_name='City')),
                ('region', models.CharField(choices=[('D', 'dolnośląskie'), ('C', 'kujawsko-pomorskie'), ('L', 'lubelskie'), ('F', 'lubuskie'), ('E', 'łódzkie'), ('K', 'małopolskie'), ('W', 'mazowieckie'), ('O', 'opolskie'), ('R', 'podkarpacke'), ('B', 'podlaskie'), ('G', 'pomorskie'), ('S', 'śląskie'), ('T', 'świętokrzskie'), ('N', 'warmińsko-mazursie'), ('P', 'wielkopolskie'), ('Z', 'zachodniopomorsie')], help_text='Choose region', max_length=1, verbose_name='Region')),
                ('zip_code', models.TextField(help_text='Enter ZIP code', max_length=8, verbose_name='ZIP code')),
                ('street', models.TextField(max_length=64, null=True)),
                ('active', models.BooleanField(default=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(help_text='You can choose many categories', to='poster.Category', verbose_name='Categories')),
                ('photos', models.ManyToManyField(help_text='You can choose many photos', to='poster.Photo', verbose_name='Photos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]