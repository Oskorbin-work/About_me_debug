# Generated by Django 4.1.7 on 2023-03-25 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_remove_gradeeducation_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gradeeducation',
            options={'ordering': ('translations__name',)},
        ),
        migrations.RenameField(
            model_name='gradeeducationtranslation',
            old_name='comment',
            new_name='commentary',
        ),
    ]
