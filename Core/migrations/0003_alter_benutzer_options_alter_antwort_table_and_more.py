# Generated by Django 4.2.5 on 2023-10-12 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_alter_benutzer__role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benutzer',
            options={'managed': False},
        ),
        migrations.AlterModelTable(
            name='antwort',
            table='Antwort',
        ),
        migrations.AlterModelTable(
            name='frage',
            table='Frage',
        ),
        migrations.AlterModelTable(
            name='kommentar',
            table='Kommentar',
        ),
    ]
