# Generated by Django 3.1.7 on 2023-02-26 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0060_alter_first_speaker_choices_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talkproposal',
            old_name='willing_to_attend_in_person',
            new_name='attend_in_person',
        ),
        migrations.RenameField(
            model_name='tutorialproposal',
            old_name='willing_to_attend_in_person',
            new_name='attend_in_person',
        ),
    ]
