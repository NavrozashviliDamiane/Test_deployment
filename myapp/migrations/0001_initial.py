# Generated by Django 4.1.7 on 2023-02-22 07:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzeria_name', models.CharField(max_length=200)),
                ('street', models.CharField(blank=True, max_length=400)),
                ('city', models.CharField(blank=True, max_length=400)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zip_code', models.IntegerField(blank=True, default=0)),
                ('website', models.URLField(blank=True, max_length=420)),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{9,10}$')])),
                ('description', models.TextField(blank=True)),
                ('logo_image', models.ImageField(blank=True, default='pizzariaImages/pizzalogo.png', upload_to='pizzariaImages')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='photos')),
                ('image_title', models.CharField(blank=True, max_length=120)),
                ('uploded_at', models.DateTimeField(auto_now_add=True)),
                ('pizzeria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizzeria_images', to='myapp.pizzeria')),
            ],
            options={
                'ordering': ['-uploded_at'],
            },
        ),
    ]