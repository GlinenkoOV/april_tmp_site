# Generated by Django 4.2 on 2023-04-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_unlimited'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('subtopic', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('is_visible', models.BooleanField(default=True)),
                ('desc', models.TextField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]