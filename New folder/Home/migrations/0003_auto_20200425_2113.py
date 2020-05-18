# Generated by Django 3.0.4 on 2020-04-25 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imageFile', '0008_test'),
        ('Home', '0002_getmodel_connkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getmodel',
            name='connKey',
        ),
        migrations.AddField(
            model_name='getmodel',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='imageFile.Test'),
        ),
    ]
