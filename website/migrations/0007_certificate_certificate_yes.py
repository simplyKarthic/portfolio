# Generated by Django 3.2.7 on 2021-11-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20211126_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='Certificate_yes',
            field=models.BooleanField(default=False),
        ),
    ]
