# Generated by Django 3.2.7 on 2021-11-26 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Intro',
            new_name='home',
        ),
        migrations.DeleteModel(
            name='Certificates',
        ),
        migrations.DeleteModel(
            name='Coding_skils',
        ),
        migrations.DeleteModel(
            name='Education_experience',
        ),
        migrations.DeleteModel(
            name='Fetured_Work',
        ),
    ]