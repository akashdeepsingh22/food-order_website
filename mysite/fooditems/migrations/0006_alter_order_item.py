# Generated by Django 5.1.4 on 2025-01-09 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooditems', '0005_order_item_order_quantity_delete_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='fooditems.item'),
        ),
    ]
