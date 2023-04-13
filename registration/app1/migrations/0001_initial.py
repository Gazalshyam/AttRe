# Generated by Django 4.0.2 on 2023-04-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=35)),
                ('programme', models.CharField(max_length=20)),
                ('hostel_name', models.CharField(max_length=20)),
                ('room_no', models.CharField(max_length=6)),
                ('roll_no', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=50)),
                ('hindi_name', models.CharField(max_length=100)),
                ('fathers_name', models.CharField(max_length=50)),
                ('date_of_payment', models.DateTimeField()),
                ('transaction_number', models.CharField(max_length=17)),
                ('address', models.TextField(max_length=500)),
                ('address2', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=50)),
                ('sem_reg', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('pincode', models.IntegerField()),
                ('sgpi', models.FloatField(max_length=5)),
                ('cgpi', models.FloatField(max_length=5)),
            ],
        ),
    ]
