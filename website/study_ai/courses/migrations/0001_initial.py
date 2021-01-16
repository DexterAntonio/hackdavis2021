# Generated by Django 3.1.5 on 2021-01-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('requirements', models.CharField(max_length=500)),
                ('requirements_json_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('webpage', models.CharField(max_length=200)),
                ('requirements', models.ManyToManyField(to='courses.Achievment')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('course_number', models.CharField(max_length=10)),
                ('prereqs', models.ManyToManyField(related_name='_course_prereqs_+', to='courses.Course')),
            ],
        ),
    ]