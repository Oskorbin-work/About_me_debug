# Generated by Django 4.1.7 on 2023-07-23 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_1_sending_emails', '0009_emailuser_emailusertranslation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailUser',
            new_name='MessageEmail',
        ),
        migrations.RenameModel(
            old_name='EmailUserTranslation',
            new_name='MessageEmailTranslation',
        ),
        migrations.AlterModelOptions(
            name='messageemailtranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'message email Translation'},
        ),
        migrations.AlterModelTable(
            name='messageemailtranslation',
            table='project_1_sending_emails_messageemail_translation',
        ),
    ]
