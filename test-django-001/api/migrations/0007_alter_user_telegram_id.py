# Generated by Django 4.1.5 on 2023-01-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_user_telegram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
