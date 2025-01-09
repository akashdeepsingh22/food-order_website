# Generated by Django 5.1.4 on 2025-01-09 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooditems', '0004_alter_order_address_alter_order_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='fooditems.item'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
