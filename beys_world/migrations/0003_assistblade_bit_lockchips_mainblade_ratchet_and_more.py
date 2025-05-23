# Generated by Django 5.1.7 on 2025-03-16 23:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beys_world', '0002_alter_blade_stat_attack_alter_blade_stat_defense_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssistBlade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(default='N/A', max_length=50, verbose_name='Abbreviation')),
                ('name', models.CharField(default='N/A', max_length=50, verbose_name='Hasbro Name')),
                ('image', models.ImageField(blank=True, upload_to='pictures/blades/%Y/%m/%d', verbose_name='Image')),
                ('type_bey', models.CharField(default='N/A', max_length=50, verbose_name='Type')),
                ('spin_direction', models.CharField(default='N/A', max_length=50, verbose_name='Spin Direction')),
                ('weight', models.FloatField(blank=True, default=None, null=True, verbose_name='Weight')),
                ('system_bey', models.CharField(default='N/A', max_length=50, verbose_name='System')),
                ('link_fandom', models.CharField(max_length=100, verbose_name='Link Fandom')),
                ('show', models.BooleanField(default=True, verbose_name='Show')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Assist Blade',
                'verbose_name_plural': 'Assist Blades',
            },
        ),
        migrations.CreateModel(
            name='Bit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(default='N/A', max_length=50, verbose_name='Abbreviation')),
                ('name', models.CharField(default='N/A', max_length=50, verbose_name='Name')),
                ('image', models.ImageField(blank=True, upload_to='pictures/blades/%Y/%m/%d', verbose_name='Image')),
                ('type_bey', models.CharField(default='N/A', max_length=50, verbose_name='Type')),
                ('spin_direction', models.CharField(default='N/A', max_length=50, verbose_name='Spin Direction')),
                ('weight', models.FloatField(blank=True, default=None, null=True, verbose_name='Weight')),
                ('system_bey', models.CharField(default='N/A', max_length=50, verbose_name='System')),
                ('stat_attack', models.IntegerField(blank=True, null=True, verbose_name='Attack')),
                ('stat_defense', models.IntegerField(blank=True, null=True, verbose_name='Defense')),
                ('stat_stamina', models.IntegerField(blank=True, null=True, verbose_name='Stamina')),
                ('stat_burst', models.IntegerField(blank=True, null=True, verbose_name='Burst Resistance')),
                ('stat_dash', models.IntegerField(blank=True, null=True, verbose_name='dash')),
                ('link_fandom', models.CharField(max_length=100, verbose_name='Link Fandom')),
                ('show', models.BooleanField(default=True, verbose_name='Show')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Bit',
                'verbose_name_plural': 'Bits',
            },
        ),
        migrations.CreateModel(
            name='LockChips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_takara', models.CharField(default='N/A', max_length=50, verbose_name='Takara Tomy Name')),
                ('name_hasbro', models.CharField(default='N/A', max_length=50, verbose_name='Hasbro Name')),
                ('image', models.ImageField(blank=True, upload_to='pictures/blades/%Y/%m/%d', verbose_name='Image')),
                ('spin_direction', models.CharField(default='N/A', max_length=50, verbose_name='Spin Direction')),
                ('weight', models.FloatField(blank=True, default=None, null=True, verbose_name='Weight')),
                ('system_bey', models.CharField(default='N/A', max_length=50, verbose_name='System')),
                ('link_fandom', models.CharField(max_length=100, verbose_name='Link Fandom')),
                ('show', models.BooleanField(default=True, verbose_name='Show')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Lock Chip',
                'verbose_name_plural': 'Lock Chips',
            },
        ),
        migrations.CreateModel(
            name='MainBlade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_takara', models.CharField(default='N/A', max_length=50, verbose_name='Takara Tomy Name')),
                ('name_hasbro', models.CharField(default='N/A', max_length=50, verbose_name='Hasbro Name')),
                ('image', models.ImageField(blank=True, upload_to='pictures/blades/%Y/%m/%d', verbose_name='Image')),
                ('type_bey', models.CharField(default='N/A', max_length=50, verbose_name='Type')),
                ('spin_direction', models.CharField(default='N/A', max_length=50, verbose_name='Spin Direction')),
                ('weight', models.FloatField(blank=True, default=None, null=True, verbose_name='Weight')),
                ('system_bey', models.CharField(default='N/A', max_length=50, verbose_name='System')),
                ('link_fandom', models.CharField(max_length=100, verbose_name='Link Fandom')),
                ('show', models.BooleanField(default=True, verbose_name='Show')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Main Blade',
                'verbose_name_plural': 'Main Blades',
            },
        ),
        migrations.CreateModel(
            name='Ratchet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(default='N/A', max_length=50, verbose_name='Abbreviation')),
                ('name', models.CharField(default='N/A', max_length=50, verbose_name='Name')),
                ('image', models.ImageField(blank=True, upload_to='pictures/blades/%Y/%m/%d', verbose_name='Image')),
                ('type_bey', models.CharField(default='N/A', max_length=50, verbose_name='Type')),
                ('spin_direction', models.CharField(default='N/A', max_length=50, verbose_name='Spin Direction')),
                ('weight', models.FloatField(blank=True, default=None, null=True, verbose_name='Weight')),
                ('system_bey', models.CharField(default='N/A', max_length=50, verbose_name='System')),
                ('stat_attack', models.IntegerField(blank=True, null=True, verbose_name='Attack')),
                ('stat_defense', models.IntegerField(blank=True, null=True, verbose_name='Defense')),
                ('stat_stamina', models.IntegerField(blank=True, null=True, verbose_name='Stamina')),
                ('link_fandom', models.CharField(max_length=100, verbose_name='Link Fandom')),
                ('show', models.BooleanField(default=True, verbose_name='Show')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Ratchet',
                'verbose_name_plural': 'Ratchets',
            },
        ),
        migrations.RenameField(
            model_name='blade',
            old_name='name_Hasbro',
            new_name='name_hasbro',
        ),
        migrations.AlterField(
            model_name='blade',
            name='weight',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Weight'),
        ),
    ]
