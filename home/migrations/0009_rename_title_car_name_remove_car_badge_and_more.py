# Generated by Django 5.1.4 on 2025-01-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_name_car_title_remove_car_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='car',
            name='badge',
        ),
        migrations.RemoveField(
            model_name='car',
            name='fuel',
        ),
        migrations.RemoveField(
            model_name='car',
            name='mileage',
        ),
        migrations.RemoveField(
            model_name='car',
            name='price',
        ),
        migrations.RemoveField(
            model_name='car',
            name='seats',
        ),
        migrations.RemoveField(
            model_name='car',
            name='transmission',
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='features',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car_images/'),
        ),
    ]
