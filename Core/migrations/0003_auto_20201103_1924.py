# Generated by Django 2.2.14 on 2020-11-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_auto_20201101_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery ', 'Cash On Delivery '), ('Khlati ', 'Khlati ')], default='Cash On Delivery ', max_length=20),
        ),
    ]
