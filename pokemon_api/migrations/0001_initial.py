# Generated by Django 3.1.2 on 2020-11-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_evolution', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=120)),
                ('evolution_type', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pokemon', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=120)),
                ('base_stats', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('evolutions', models.ManyToManyField(blank=True, to='pokemon_api.Evolution')),
            ],
        ),
    ]
