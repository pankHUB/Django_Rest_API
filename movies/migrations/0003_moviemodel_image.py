# Generated by Django 3.1.7 on 2021-06-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviemodel_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='image',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
