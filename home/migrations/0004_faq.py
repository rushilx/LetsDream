# Generated by Django 5.1.4 on 2025-01-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
    ]
