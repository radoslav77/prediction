# Generated by Django 4.1 on 2023-05-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DATA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_drow', models.CharField(max_length=400)),
                ('ball1', models.IntegerField()),
                ('ball2', models.IntegerField()),
                ('ball3', models.IntegerField()),
                ('ball4', models.IntegerField()),
                ('ball5', models.IntegerField()),
                ('lucky1', models.IntegerField()),
                ('lucky2', models.IntegerField()),
            ],
        ),
    ]
