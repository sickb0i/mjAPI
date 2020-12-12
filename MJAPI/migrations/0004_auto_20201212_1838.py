# Generated by Django 3.1.4 on 2020-12-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MJAPI', '0003_auto_20201212_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='customer',
            name='zip',
            field=models.IntegerField(default=69001),
        ),
        migrations.AddField(
            model_name='deliverypartner',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='deliverypartner',
            name='city',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='deliverypartner',
            name='zip',
            field=models.IntegerField(default=69001),
        ),
        migrations.AddField(
            model_name='retailer',
            name='city',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='retailer',
            name='zip',
            field=models.IntegerField(default=69001),
        ),
        migrations.AlterField(
            model_name='category',
            name='glyph',
            field=models.ImageField(default='', upload_to='glyphs/'),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
