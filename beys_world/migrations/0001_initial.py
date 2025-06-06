# Generated by Django 5.1.7 on 2025-03-13 11:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_takara', models.CharField(default='N/A', max_length=50, verbose_name='Takara Tomy Name')),
                ('name_Hasbro', models.CharField(default='N/A', max_length=50, verbose_name='Hasbro Name')),
                ('image', models.ImageField(blank=True, upload_to='pictures/blades/%Y/%m/%d', verbose_name='Image')),
                ('type_bey', models.CharField(default='N/A', max_length=50, verbose_name='Type')),
                ('spin_direction', models.CharField(default='N/A', max_length=50, verbose_name='Spin Direction')),
                ('weight', models.FloatField(blank=True, verbose_name='Weight')),
                ('system_bey', models.CharField(default='N/A', max_length=50, verbose_name='System')),
                ('stat_attack', models.IntegerField(blank=True, verbose_name='Attack')),
                ('stat_defense', models.IntegerField(blank=True, verbose_name='Defense')),
                ('stat_stamina', models.IntegerField(blank=True, verbose_name='Stamina')),
                ('link_fandom', models.CharField(max_length=100, verbose_name='Link Fandom')),
                ('show', models.BooleanField(default=True, verbose_name='Show')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Blade',
                'verbose_name_plural': 'Blades',
            },
        ),
    ]
