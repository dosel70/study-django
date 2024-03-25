# Generated by Django 5.0.2 on 2024-02-20 16:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_title', models.CharField(max_length=50)),
                ('post_content', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'tbl_post',
                'ordering': ['-id'],
            },
        ),
    ]
