# Generated by Django 4.1.2 on 2022-10-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_Number', models.CharField(max_length=25)),
                ('Vehicle_Type', models.CharField(choices=[('Two wheeler', 'Two wheeler'), ('Three wheeler', 'Three wheeler'), ('Four wheeler', 'Four wheeler')], max_length=255, null=True)),
                ('Vehicle_Model', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
