# Generated by Django 4.0.4 on 2022-06-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('contenido', models.TextField(max_length=3000)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
