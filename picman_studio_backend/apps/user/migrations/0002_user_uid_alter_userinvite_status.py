# Generated by Django 4.0.5 on 2022-06-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userinvite',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Invited'), (2, 'Pending'), (3, 'Accepted')], default=1, null=True),
        ),
    ]
