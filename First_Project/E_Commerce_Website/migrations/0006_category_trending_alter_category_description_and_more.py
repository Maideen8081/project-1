# Generated by Django 5.1.3 on 2024-11-14 12:50

import E_Commerce_Website.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce_Website', '0005_rename_database1_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='trending',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vendar', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=E_Commerce_Website.models.filename)),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('trending', models.BooleanField(default=False)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Commerce_Website.category')),
            ],
        ),
    ]
