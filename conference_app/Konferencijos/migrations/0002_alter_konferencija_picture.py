# Generated by Django 4.2.2 on 2023-06-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Konferencijos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konferencija',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
