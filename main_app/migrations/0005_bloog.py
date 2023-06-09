# Generated by Django 4.2 on 2023-04-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('is_visible', models.BooleanField(default=True)),
                ('desc', models.TextField(max_length=200)),
                ('author', models.TextField(max_length=200)),
                ('date', models.DateField()),
                ('photo', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
