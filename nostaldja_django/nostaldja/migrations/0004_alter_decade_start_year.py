# Generated by Django 4.0.4 on 2022-05-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0003_alter_fad_description_alter_fad_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decade',
            name='start_year',
            field=models.CharField(max_length=500),
        ),
    ]
