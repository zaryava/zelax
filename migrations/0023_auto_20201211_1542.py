# Generated by Django 3.1.3 on 2020-12-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubajax', '0022_auto_20201211_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataubntall',
            name='udnagrl',
            field=models.FloatField(default=0.0, verbose_name='Трафик приема локального РРС'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataubntall',
            name='udnagrl_mk',
            field=models.CharField(default=0.0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataubntall',
            name='udnagrr',
            field=models.FloatField(default=0.0, verbose_name='Трафик приема удалённого РРС'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataubntall',
            name='udnagrr_mk',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
