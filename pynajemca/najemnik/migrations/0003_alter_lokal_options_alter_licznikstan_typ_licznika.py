# Generated by Django 4.0.3 on 2022-04-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('najemnik', '0002_remove_lokal_kubatura'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lokal',
            options={'ordering': ('numer_lokalu',)},
        ),
        migrations.AlterField(
            model_name='licznikstan',
            name='typ_licznika',
            field=models.IntegerField(choices=[(1, 'Woda'), (2, 'Ciepło')], default=1),
        ),
    ]
