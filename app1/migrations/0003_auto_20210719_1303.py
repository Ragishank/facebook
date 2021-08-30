# Generated by Django 3.2.4 on 2021-07-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]