# Generated by Django 3.2.7 on 2021-11-04 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flytofasto_api', '0008_auto_20211104_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_city',
            field=models.ForeignKey(db_column='arrival_city_id', on_delete=django.db.models.deletion.CASCADE, related_name='arrival_city_id', to='flytofasto_api.city'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.ForeignKey(db_column='departure_city_id', on_delete=django.db.models.deletion.CASCADE, related_name='departure_city_id', to='flytofasto_api.city'),
        ),
    ]
