# Generated by Django 4.1 on 2022-08-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostWorking', '0008_remove_workinfor_phonenumber_workinfor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workinfor',
            name='Level',
            field=models.CharField(choices=[('intership', 'intership'), ('fresher', 'fresher'), ('senior', 'senior'), ('junior', 'junior')], default='intership', max_length=200),
        ),
        migrations.AlterField(
            model_name='workinfor',
            name='LongTime',
            field=models.CharField(choices=[('3 hours', '3 hours'), ('12 hours', '12 hours'), ('2 days', '2 days')], default='3 hours', max_length=200),
        ),
        migrations.AlterField(
            model_name='workinfor',
            name='photo',
            field=models.ImageField(blank=True, default=None, upload_to='WorkImages'),
        ),
    ]
