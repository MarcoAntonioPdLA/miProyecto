# Generated by Django 3.2.3 on 2021-05-31 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20210531_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='donador',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]