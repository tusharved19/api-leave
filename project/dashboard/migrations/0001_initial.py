# Generated by Django 3.2.7 on 2021-10-11 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'department',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contactnum', models.IntegerField()),
                ('email', models.EmailField(max_length=30, null=True)),
                ('employeeid', models.CharField(blank=True, max_length=5, null=True, verbose_name='Employee Id Number')),
                ('salary', models.FloatField(default=0, max_length=10)),
                ('allowed_leave', models.IntegerField(default=1)),
                ('applied_leaves', models.IntegerField(null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.department', verbose_name='department')),
            ],
            options={
                'verbose_name': 'Employee',
            },
        ),
    ]
