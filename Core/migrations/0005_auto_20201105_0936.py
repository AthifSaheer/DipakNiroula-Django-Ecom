# Generated by Django 2.2.14 on 2020-11-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_auto_20201104_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery ', 'Cash On Delivery '), ('Khalti ', 'Khalti '), ('Esewa ', 'Esewa ')], default='Khalti', max_length=20),
        ),
    ]
