# Generated by Django 4.0.3 on 2022-03-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NameExperiments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_experiments_file', models.CharField(max_length=200)),
                ('is_running', models.BooleanField(default=False)),
                ('is_finished', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]