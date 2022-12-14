# Generated by Django 4.1 on 2022-09-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostWorking', '0010_alter_workinfor_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workinfor',
            name='money',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=12),
        ),
        migrations.AlterField(
            model_name='workinfor',
            name='photo',
            field=models.ImageField(blank=True, default='../WorkImages/default-image.jpg', upload_to='WorkImages'),
        ),
    ]
