# Generated by Django 4.1.7 on 2023-07-17 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_1_sending_emails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailEnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailRecipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
        migrations.DeleteModel(
            name='TemplateEmail',
        ),
        migrations.AddField(
            model_name='emailend',
            name='body',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project_1_sending_emails.emailtemplate'),
        ),
        migrations.AddField(
            model_name='emailend',
            name='recipients',
            field=models.ManyToManyField(blank=True, null=True, to='project_1_sending_emails.emailrecipient'),
        ),
    ]
