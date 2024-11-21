# Generated by Django 5.1.3 on 2024-11-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
