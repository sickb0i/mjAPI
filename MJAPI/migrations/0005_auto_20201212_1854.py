# Generated by Django 3.1.4 on 2020-12-12 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MJAPI', '0004_auto_20201212_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MJAPI.contact'),
        ),
        migrations.AlterField(
            model_name='deliverypartner',
            name='contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MJAPI.contact'),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MJAPI.contact'),
        ),
    ]
