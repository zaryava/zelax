# Generated by Django 3.0.5 on 2020-04-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubajax', '0006_ubntmodeltest_current_list_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listipubnt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_list_ip', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='ubntmodeltest',
            name='current_list_ip',
        ),
    ]
