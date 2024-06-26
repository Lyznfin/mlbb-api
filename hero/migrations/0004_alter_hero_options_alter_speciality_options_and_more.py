# Generated by Django 5.0.3 on 2024-04-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_alter_hero_hero_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hero',
            options={'verbose_name_plural': 'Heroes'},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name_plural': 'Specialities'},
        ),
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.TextField(max_length=500, unique=True),
        ),
    ]
