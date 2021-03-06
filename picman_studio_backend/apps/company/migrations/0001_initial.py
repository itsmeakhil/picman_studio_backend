# Generated by Django 4.0.5 on 2022-06-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('company_id', models.CharField(default='COMP_8IP5629WJ9', editable=False, max_length=20)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'COMPANY',
            },
        ),
    ]
