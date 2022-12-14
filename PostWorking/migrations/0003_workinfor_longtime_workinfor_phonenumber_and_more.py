# Generated by Django 4.1 on 2022-08-08 08:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostWorking', '0002_workinfor_description_text_workinfor_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workinfor',
            name='LongTime',
            field=models.CharField(choices=[('1', '3 hours'), ('2', '12 hours'), ('3', '2 days')], default='3 hours', max_length=200),
        ),
        migrations.AddField(
            model_name='workinfor',
            name='Phonenumber',
            field=models.CharField(default=None, max_length=11, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AddField(
            model_name='workinfor',
            name='money',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=12),
        ),
        migrations.AddField(
            model_name='workinfor',
            name='photo',
            field=models.ImageField(default=None, upload_to='WorkImages'),
        ),
        migrations.AlterField(
            model_name='workinfor',
            name='Company_text',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='workinfor',
            name='Description_text',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='workinfor',
            name='WorkName_text',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
