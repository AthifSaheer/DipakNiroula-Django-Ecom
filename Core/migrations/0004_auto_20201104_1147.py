# Generated by Django 2.2.14 on 2020-11-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_auto_20201103_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery ', 'Cash On Delivery '), ('Khalti ', 'Khalti ')], default='Cash On Delivery ', max_length=20),
        ),
    ]
