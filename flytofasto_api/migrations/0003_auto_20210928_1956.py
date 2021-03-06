# Generated by Django 3.2.7 on 2021-09-29 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flytofasto_api', '0002_alter_customer_document_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('seats', models.PositiveIntegerField()),
                ('airline', models.ForeignKey(db_column='airline_id', on_delete=django.db.models.deletion.CASCADE, to='flytofasto_api.airline')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('level_reference', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('customer', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='flytofasto_api.customer')),
                ('flight', models.ForeignKey(db_column='flight_id', on_delete=django.db.models.deletion.CASCADE, to='flytofasto_api.flight')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='location_from',
            field=models.ForeignKey(db_column='location_id_from', on_delete=django.db.models.deletion.CASCADE, related_name='location_id_from', to='flytofasto_api.location'),
        ),
        migrations.AddField(
            model_name='flight',
            name='location_to',
            field=models.ForeignKey(db_column='location_id_to', on_delete=django.db.models.deletion.CASCADE, related_name='location_id_to', to='flytofasto_api.location'),
        ),
        migrations.CreateModel(
            name='Credit_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=255, unique=True)),
                ('card_type', models.CharField(max_length=255)),
                ('expiration_year', models.PositiveIntegerField()),
                ('expiration_month', models.PositiveIntegerField()),
                ('security_code', models.PositiveIntegerField()),
                ('customer', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='flytofasto_api.customer')),
            ],
        ),
    ]
