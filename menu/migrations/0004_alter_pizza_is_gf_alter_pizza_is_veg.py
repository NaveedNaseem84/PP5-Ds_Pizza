# Generated by Django 4.2.21 on 2025-06-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='is_gf',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='is_veg',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
    ]
