# Generated by Django 3.0.4 on 2020-04-03 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200401_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitemimage',
            name='product_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_item_images', to='products.ProductItem'),
        ),
    ]