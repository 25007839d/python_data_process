# Generated by Django 4.1.3 on 2022-11-26 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='eid',
        ),
    ]