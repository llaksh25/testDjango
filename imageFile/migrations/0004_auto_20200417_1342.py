# Generated by Django 3.0.4 on 2020-04-17 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageFile', '0003_auto_20200417_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='imageColumn',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]