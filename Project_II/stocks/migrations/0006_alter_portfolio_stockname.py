# Generated by Django 4.2.5 on 2023-10-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_portfolio_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='stockname',
            field=models.CharField(max_length=100),
        ),
    ]
