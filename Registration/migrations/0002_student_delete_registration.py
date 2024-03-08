# Generated by Django 5.0.3 on 2024-03-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
