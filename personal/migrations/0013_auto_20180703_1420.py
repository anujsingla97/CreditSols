# Generated by Django 2.0.6 on 2018-07-03 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0012_auto_20180703_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedloan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.PersonalInfo'),
        ),
        migrations.AlterField(
            model_name='currentloan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.PersonalInfo'),
        ),
    ]
