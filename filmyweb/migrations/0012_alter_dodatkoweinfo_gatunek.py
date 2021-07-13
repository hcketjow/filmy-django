# Generated by Django 3.2.4 on 2021-07-13 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0011_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (2, 'Komedia'), (5, 'Przygodowy'), (4, 'Drama'), (1, 'Horror'), (3, 'Sci-fi'), (5, 'Akcja')], default=0),
        ),
    ]