# Generated by Django 3.1.2 on 2020-11-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20201107_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
