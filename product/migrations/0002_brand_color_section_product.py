# Generated by Django 5.0.2 on 2024-02-26 09:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('top_deals_of_the_day', 'Top Deals Of The Day'), ('top_selling_products', 'Top Selling Products'), ('top_featured_products', 'Top Featured Products'), ('recommended', 'Recommended')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='', max_length=100, null=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_details', models.TextField()),
                ('description', models.TextField()),
                ('total_availability', models.IntegerField()),
                ('featured_image', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('product_status', models.CharField(choices=[('brand_new', 'Brand New'), ('recently_used', 'Recently Used'), ('used', 'Used'), ('old', 'Old')], default='brand_new', max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.color')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.section')),
            ],
        ),
    ]
