# Generated by Django 3.2.11 on 2022-11-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('envs', models.CharField(max_length=128)),
                ('startAt', models.DateField(null=True)),
            ],
        ),
    ]
