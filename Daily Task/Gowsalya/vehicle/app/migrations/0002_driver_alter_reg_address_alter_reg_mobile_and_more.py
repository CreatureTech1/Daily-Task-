# Generated by Django 4.1.1 on 2022-09-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('dob', models.DateField()),
                ('address', models.TextField(max_length=50)),
                ('driving_license', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='reg',
            name='address',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reg',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reg',
            name='registration_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reg',
            name='year',
            field=models.IntegerField(),
        ),
    ]
