# Generated by Django 4.1.7 on 2023-04-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_projectskills_skill_skilltranslation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='img',
            field=models.ImageField(blank=True, height_field=100, upload_to='skills/', width_field=100),
        ),
    ]
