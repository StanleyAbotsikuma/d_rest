# Generated by Django 3.2.13 on 2023-04-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=40)),
                ('password', models.TextField(max_length=40)),
                ('randoms', models.CharField(max_length=100)),
                ('upload', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
