# Generated by Django 3.0.1 on 2020-01-25 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('mat_id', models.AutoField(primary_key=True, serialize=False)),
                ('mat_link', models.CharField(max_length=255)),
                ('mat_description', models.CharField(max_length=255)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_portal.Course')),
            ],
        ),
    ]