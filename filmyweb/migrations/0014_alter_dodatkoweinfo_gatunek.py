# Generated by Django 3.2.4 on 2021-07-13 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0013_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(5, 'Akcja'), (2, 'Komedia'), (5, 'Przygodowy'), (3, 'Sci-fi'), (1, 'Horror'), (0, 'Inne'), (4, 'Drama')], default=0),
        ),
    ]
