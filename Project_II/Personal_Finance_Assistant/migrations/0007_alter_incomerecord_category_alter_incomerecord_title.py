# Generated by Django 4.2.5 on 2023-10-04 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_Finance_Assistant', '0006_alter_incomerecord_category_alter_incomerecord_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomerecord',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='incomerecord',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
