# Generated by Django 3.2.4 on 2021-07-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0027_auto_20210730_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (0, 'Inne'), (3, 'Sci-fi'), (5, 'Akcja'), (6, 'Przygodowy'), (4, 'Drama'), (2, 'Komedia')], default=0),
        ),
    ]
