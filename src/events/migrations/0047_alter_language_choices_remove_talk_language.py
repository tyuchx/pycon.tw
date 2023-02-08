# Generated by Django 3.1.7 on 2023-02-08 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0046_alter_prefer_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsoredevent',
            name='talk_language',
        ),
        migrations.AlterField(
            model_name='sponsoredevent',
            name='language',
            field=models.CharField(choices=[('ENEN', 'English talk'), ('ZHEN', 'Chinese talk w. English slides'), ('ZHZH', 'Chinese talk w. Chinese slides'), ('TAI', 'Taiwanese Hokkien')], max_length=5, verbose_name='language'),
        ),
    ]
