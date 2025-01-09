# Generated by Django 5.1.4 on 2025-01-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooditems', '0003_remove_order_item_order_address_order_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
