# Generated by Django 4.1 on 2022-08-08 09:12

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('PostWorking', '0003_workinfor_longtime_workinfor_phonenumber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workinfor',
            name='Phonenumber',
        ),
        migrations.AddField(
            model_name='workinfor',
            name='PhoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None),
        ),
    ]