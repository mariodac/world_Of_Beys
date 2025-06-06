# Generated by Django 5.1.7 on 2025-03-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beys_world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blade',
            name='stat_attack',
            field=models.IntegerField(blank=True, null=True, verbose_name='Attack'),
        ),
        migrations.AlterField(
            model_name='blade',
            name='stat_defense',
            field=models.IntegerField(blank=True, null=True, verbose_name='Defense'),
        ),
        migrations.AlterField(
            model_name='blade',
            name='stat_stamina',
            field=models.IntegerField(blank=True, null=True, verbose_name='Stamina'),
        ),
        migrations.AlterField(
            model_name='blade',
            name='weight',
            field=models.FloatField(blank=True, null=True, verbose_name='Weight'),
        ),
    ]
