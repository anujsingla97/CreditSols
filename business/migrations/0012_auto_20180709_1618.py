# Generated by Django 2.0.6 on 2018-07-09 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0011_auto_20180709_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.BusinessAccount'),
        ),
    ]