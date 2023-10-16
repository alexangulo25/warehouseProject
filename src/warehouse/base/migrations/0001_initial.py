# Generated by Django 4.2.5 on 2023-10-04 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('LastModified', models.DateTimeField(auto_now_add=True)),
                ('WarehouseId', models.CharField(max_length=200)),
            ],
        ),
    ]
