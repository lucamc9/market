# Generated by Django 2.0 on 2018-06-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_nicname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nicname',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
    ]
