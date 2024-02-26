# Generated by Django 5.0.2 on 2024-02-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(choices=[('Top Deals Of The Day', 'Top Deals Of The Day'), ('Top Selling Products', 'Top Selling Products'), ('Recommended', 'Recommended')], max_length=200),
        ),
    ]