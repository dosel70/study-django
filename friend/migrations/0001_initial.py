# Generated by Django 5.0.2 on 2024-02-22 15:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0005_alter_member_member_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.SmallIntegerField(choices=[(0, '친구'), (-1, '거절'), (1, '대기')], default=0)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receiver_set', to='member.member')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sender_set', to='member.member')),
            ],
            options={
                'db_table': 'tbl_friend',
            },
        ),
    ]
