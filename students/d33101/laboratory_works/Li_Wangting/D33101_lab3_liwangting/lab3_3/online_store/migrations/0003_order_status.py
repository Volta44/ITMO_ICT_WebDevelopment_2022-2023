# Generated by Django 4.0.3 on 2022-03-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0002_order_product_useroforder_productsoforder'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('c', 'created'), ('i', 'Invalid')], default='c', max_length=1, verbose_name='status'),
        ),
    ]
