# Generated by Django 4.2.4 on 2024-07-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0007_alter_stock_in_stock_alter_stock_out_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='in_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='out_stock',
            field=models.IntegerField(default=0),
        ),
    ]