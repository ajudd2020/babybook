# Generated by Django 3.1 on 2020-08-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='babybookentry',
            name='image_caption',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
