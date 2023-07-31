# Generated by Django 4.2.1 on 2023-06-13 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Konferencijos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Renginys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('visitors', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('konferencija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Konferencijos.konferencija')),
            ],
        ),
        migrations.CreateModel(
            name='RenginysRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('renginys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Renginiai.renginys')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KompanijosRegistracija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kompanijos_pavadinimas', models.CharField(max_length=100)),
                ('dalyvių_skaičius', models.IntegerField(blank=True, null=True)),
                ('pastabos', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('renginys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Renginiai.renginys')),
            ],
        ),
    ]