# Generated by Django 4.2.3 on 2023-09-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_brand_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon_Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
            ],
        ),
    ]