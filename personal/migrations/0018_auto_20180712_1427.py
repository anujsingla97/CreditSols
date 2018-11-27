# Generated by Django 2.0.6 on 2018-07-12 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0012_auto_20180709_1618'),
        ('personal', '0017_duesinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='duesinfo',
            name='bank',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='business.BusinessAccount'),
        ),
        migrations.AlterField(
            model_name='duesinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.PersonalAccount'),
        ),
    ]