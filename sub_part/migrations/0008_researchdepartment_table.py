# Generated by Django 4.0.4 on 2022-05-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0007_rename_regular_temporary_nonteachingstaff_table_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='researchdepartment_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_principle_investigator', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('sanctioned_letter_number_with_date', models.CharField(max_length=100)),
                ('project_title', models.CharField(max_length=100)),
                ('duration_of_the_project', models.CharField(max_length=100)),
                ('total_sanctioned_amount', models.CharField(max_length=100)),
                ('logger_id', models.IntegerField()),
            ],
        ),
    ]
