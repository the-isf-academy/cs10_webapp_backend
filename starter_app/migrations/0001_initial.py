# Generated by Django 3.1.3 on 2021-04-12 10:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_assigned_to', models.CharField(blank=True, default='', max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('label', models.CharField(max_length=8)),
                ('notes', models.TextField(max_length=200)),
                ('due_date', models.DateField(verbose_name='Date Due')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date Created')),
                ('archive', models.BooleanField(default=False)),
            ],
        ),
    ]
