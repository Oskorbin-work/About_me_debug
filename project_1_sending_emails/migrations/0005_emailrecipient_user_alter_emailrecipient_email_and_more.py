# Generated by Django 4.1.7 on 2023-07-19 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_1_sending_emails', '0004_emailtemplate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailrecipient',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='emailrecipient',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]