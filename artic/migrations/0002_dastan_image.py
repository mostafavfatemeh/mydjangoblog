# Generated by Django 3.1.7 on 2021-02-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dastan',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='default.jpg'),
        ),
    ]
