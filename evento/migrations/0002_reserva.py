# Generated by Django 5.0.7 on 2024-07-26 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evento', models.CharField(max_length=100)),
                ('a_nombre', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField(max_length=10)),
            ],
        ),
    ]
