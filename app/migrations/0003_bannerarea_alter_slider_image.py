# Generated by Django 4.2.3 on 2023-09-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_slider_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bannerarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/banner_imgs')),
                ('Discount_Deal', models.CharField(max_length=100)),
                ('Quote', models.CharField(max_length=200)),
                ('Discount', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='Image',
            field=models.ImageField(upload_to='media/slider_imgs'),
        ),
    ]
