# Generated by Django 5.0.4 on 2024-06-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impromptu_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default='service'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
