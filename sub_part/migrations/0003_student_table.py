# Generated by Django 4.0.4 on 2022-05-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_register_table_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('student_department', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('student_batch', models.CharField(max_length=100)),
            ],
        ),
    ]