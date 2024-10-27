# Generated by Django 5.1.2 on 2024-10-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('current_salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('years_of_experience', models.IntegerField(default=0)),
                ('date_of_joining', models.DateTimeField()),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
