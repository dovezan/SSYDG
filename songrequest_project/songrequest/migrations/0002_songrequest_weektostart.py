# Generated by Django 3.2.12 on 2023-08-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songrequest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songrequest',
            name='weektostart',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]