# Generated by Django 3.0.5 on 2020-07-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubajax', '0011_auto_20200705_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataubntall',
            name='ipubnttwo',
            field=models.CharField(default='0.0.0.0', max_length=50),
        ),
        migrations.AlterField(
            model_name='dataubntall',
            name='ipubnttworem',
            field=models.CharField(default='0.0.0.0', max_length=50),
        ),
        migrations.AlterField(
            model_name='dataubntall',
            name='udnagrl_mk',
            field=models.CharField(default='bts', max_length=50),
        ),
        migrations.AlterField(
            model_name='dataubntall',
            name='udnagrr_mk',
            field=models.CharField(default='bts', max_length=50),
        ),
    ]