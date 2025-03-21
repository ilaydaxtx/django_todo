# Generated by Django 5.1.5 on 2025-01-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('category', models.CharField(blank=True, choices=[('LEISURE', 'Leisure'), ('WORK', 'Work')], max_length=20, null=True)),
                ('user', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('complete', models.BooleanField(default=False, verbose_name='progress of this project')),
            ],
            options={
                'ordering': ['complete'],
            },
        ),
    ]
