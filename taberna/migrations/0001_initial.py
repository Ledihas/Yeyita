# Generated by Django 5.0.7 on 2024-07-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfrtTab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('presio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='ofertas/')),
            ],
        ),
    ]
