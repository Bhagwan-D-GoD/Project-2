# Generated by Django 4.2.5 on 2023-10-03 10:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0010_alter_portfolio_stockname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='portfolio',
            new_name='stockportfolio',
        ),
    ]
