# Generated by Django 3.2.4 on 2021-07-21 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0015_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (4, 'Drama'), (5, 'Akcja'), (0, 'Inne'), (5, 'Przygodowy'), (2, 'Komedia'), (3, 'Sci-fi')], default=0),
        ),
    ]
