# Generated by Django 5.1.3 on 2024-12-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fooditems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('decription', models.TextField()),
                ('photo', models.ImageField(upload_to='foodimages/')),
            ],
        ),
    ]