# Generated by Django 3.1.4 on 2020-12-12 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MJAPI', '0002_auto_20201212_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='glyph',
            field=models.ImageField(default='', upload_to='glyphs/'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='customer',
            name='favoriteShops',
        ),
        migrations.AddField(
            model_name='customer',
            name='favoriteShops',
            field=models.ManyToManyField(to='MJAPI.Retailer'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MJAPI.images'),
        ),
    ]
