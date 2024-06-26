# Generated by Django 5.0.3 on 2024-04-09 16:19

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=50)),
                ('hero_alias', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HeroRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durability', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('offense', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('control_effects', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('difficulty', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('hero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hero.hero')),
            ],
        ),
        migrations.CreateModel(
            name='Lane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lane_name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=255, unique=True)),
            ],
            options={
                'unique_together': {('lane_name', 'description')},
            },
        ),
        migrations.AddField(
            model_name='hero',
            name='recomended_lane',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.lane'),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=255, unique=True)),
            ],
            options={
                'unique_together': {('role_name', 'description')},
            },
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.role'),
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality_name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=255, unique=True)),
            ],
            options={
                'unique_together': {('speciality_name', 'description')},
            },
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.speciality'),
        ),
        migrations.AlterUniqueTogether(
            name='hero',
            unique_together={('hero_name', 'hero_alias')},
        ),
    ]
