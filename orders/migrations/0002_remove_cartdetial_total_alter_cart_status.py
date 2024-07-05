# Generated by Django 5.0.3 on 2024-07-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdetial',
            name='total',
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('InProgress', 'InProgress'), ('Completed', 'Completed')], max_length=20),
        ),
    ]
