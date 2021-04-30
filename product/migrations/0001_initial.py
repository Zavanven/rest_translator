# Generated by Django 3.2 on 2021-04-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sku', models.CharField(max_length=50)),
                ('id_product', models.IntegerField()),
                ('category', models.CharField(max_length=200)),
                ('shipping_class', models.IntegerField()),
                ('image_url', models.URLField(blank=True)),
                ('cena_b2b', models.FloatField()),
                ('cena_b2c', models.FloatField()),
                ('pa_color', models.CharField(blank=True, max_length=50)),
                ('pa_type', models.CharField(blank=True, max_length=50)),
                ('pa_year', models.CharField(blank=True, max_length=50)),
                ('pa_wheels', models.CharField(blank=True, max_length=50)),
                ('pa_model', models.CharField(blank=True, max_length=100)),
                ('pa_class', models.CharField(blank=True, max_length=100)),
                ('pa_brand', models.CharField(blank=True, max_length=50)),
                ('pa_battery', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
