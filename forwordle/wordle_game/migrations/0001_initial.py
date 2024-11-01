# Generated by Django 5.1.2 on 2024-10-29 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_text', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=50)),
                ('attempts', models.ManyToManyField(to='wordle_game.attempt')),
                ('correct_word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordle_game.word')),
            ],
        ),
        migrations.AddField(
            model_name='attempt',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordle_game.word'),
        ),
    ]
