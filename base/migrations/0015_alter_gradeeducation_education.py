# Generated by Django 4.1.7 on 2023-03-19 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_gradeeducation_amount_gradeeducation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradeeducation',
            name='education',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.education'),
        ),
    ]
