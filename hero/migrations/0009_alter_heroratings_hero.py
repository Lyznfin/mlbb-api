# Generated by Django 5.0.3 on 2024-04-09 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0008_alter_heroratings_options_alter_heroratings_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroratings',
            name='hero',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hero_ratings', to='hero.hero'),
        ),
    ]