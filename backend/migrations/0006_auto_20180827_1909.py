# Generated by Django 2.1 on 2018-08-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20180827_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='heatingmodel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='heatingmodel',
            name='model_name',
            field=models.CharField(max_length=200),
        ),
    ]