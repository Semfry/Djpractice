# Generated by Django 4.0.5 on 2022-07-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypages', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modname', models.CharField(max_length=100, verbose_name='name of mod')),
                ('releaseyear', models.DateField(verbose_name='release year/start of series')),
                ('game', models.CharField(max_length=100, verbose_name='name of game')),
                ('image', models.ImageField(upload_to='static/images')),
            ],
        ),
    ]