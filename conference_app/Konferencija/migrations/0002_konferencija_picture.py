# Generated by Django 4.2.1 on 2023-06-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Konferencija', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='konferencija',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
