# Generated by Django 4.2.5 on 2023-10-03 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalAPI', '0004_usermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='finalAPI.categorymodel'),
        ),
    ]
