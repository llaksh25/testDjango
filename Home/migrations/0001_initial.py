# Generated by Django 3.0.4 on 2020-03-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='getModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50, unique=True)),
                ('email_address', models.EmailField(max_length=100, null=True)),
                ('phone_number', models.IntegerField(null=True)),
            ],
        ),
    ]