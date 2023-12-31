# Generated by Django 4.1.7 on 2023-03-19 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_gradeeducation_foo_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradeeducation',
            name='foo_field',
        ),
        migrations.RemoveField(
            model_name='gradeeducationtranslation',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='gradeeducationtranslation',
            name='education',
        ),
        migrations.RemoveField(
            model_name='gradeeducationtranslation',
            name='type',
        ),
        migrations.AddField(
            model_name='gradeeducation',
            name='education',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='base.education'),
        ),
        migrations.AlterField(
            model_name='basetranslation',
            name='title',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='contentbodytranslation',
            name='title',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='educationtranslation',
            name='city',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='educationtranslation',
            name='country',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='educationtranslation',
            name='degree',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='educationtranslation',
            name='name',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='educationtranslation',
            name='specialty',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='gradeeducationtranslation',
            name='name',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='menulevonetranslation',
            name='address',
            field=models.CharField(blank=True, default='#', max_length=90),
        ),
        migrations.AlterField(
            model_name='menulevonetranslation',
            name='name',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='menulevtwotranslation',
            name='name',
            field=models.CharField(blank=True, max_length=90),
        ),
    ]
