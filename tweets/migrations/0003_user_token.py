# Generated by Django 3.0.3 on 2020-09-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20200920_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
