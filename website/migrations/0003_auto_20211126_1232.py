# Generated by Django 3.2.7 on 2021-11-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20211126_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='C_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='C_image',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='home',
            name='C_title',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='E_acquired',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='E_course',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='E_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='E_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='F_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='F_image',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='home',
            name='F_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='F_tech',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='F_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='I_descrption',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='I_hi',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='I_img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='home',
            name='I_per',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='I_resume',
            field=models.FileField(null=True, upload_to='resume'),
        ),
        migrations.AddField(
            model_name='home',
            name='I_skills',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='skills',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='skills_per',
            field=models.IntegerField(null=True),
        ),
    ]