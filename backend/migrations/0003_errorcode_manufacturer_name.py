# Generated by Django 2.1 on 2018-08-27 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20180827_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorcode',
            name='manufacturer_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.Manufacturer'),
            preserve_default=False,
        ),
    ]