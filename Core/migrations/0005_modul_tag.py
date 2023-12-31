# Generated by Django 4.2.5 on 2023-10-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_alter_benutzer_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modul',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('str_id', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'Modul',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('str_id', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'Tag',
                'managed': False,
            },
        ),
    ]
