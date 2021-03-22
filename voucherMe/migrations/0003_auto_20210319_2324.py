# Generated by Django 3.1.7 on 2021-03-19 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucherMe', '0002_auto_20210319_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('FOOD', '1'), ('TRAVEL', '2'), ('FASHION', '3'), ('TECHNOLOGY', '4'), ('BOOKS', '5'), ('MUSIC', '6'), ('FURNITURE', '7'), ('STATIONARY & ART', '8'), ('SKINCARE & BEAUTY', '9')], default=1, max_length=128),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
