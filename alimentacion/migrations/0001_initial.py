# Generated by Django 5.0.6 on 2024-05-26 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentacion',
            fields=[
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('tipo_comida', models.CharField(choices=[('desayuno', 'Desayuno'), ('almuerzo', 'Almuerzo'), ('cena', 'Cena')], max_length=50)),
                ('calorias', models.IntegerField()),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
