# Generated by Django 4.1 on 2022-09-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostWorking', '0009_alter_workinfor_level_alter_workinfor_longtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workinfor',
            name='money',
            field=models.DecimalField(decimal_places=2, default='../WorkImages/default-image.jpg', max_digits=12),
        ),
    ]