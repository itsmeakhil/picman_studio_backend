# Generated by Django 4.0.5 on 2022-06-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='COMP_YN8SU0F4N7', editable=False, max_length=20),
        ),
    ]