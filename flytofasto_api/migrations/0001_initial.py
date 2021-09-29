# Generated by Django 3.2.7 on 2021-09-29 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('document_type', models.PositiveIntegerField()),
                ('document_number', models.CharField(max_length=255)),
            ],
            options={
                'unique_together': {('document_type', 'document_number')},
            },
        ),
    ]