# Generated by Django 4.2.5 on 2023-10-03 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_portfolio_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='user',
        ),
    ]
