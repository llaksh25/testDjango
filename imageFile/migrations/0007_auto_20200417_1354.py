# Generated by Django 3.0.4 on 2020-04-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageFile', '0006_auto_20200417_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='imageColumn',
            field=models.ImageField(null=True, upload_to='imageFolder/'),
        ),
    ]
