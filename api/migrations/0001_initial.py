# Generated by Django 4.0.5 on 2022-07-04 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('rol', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('habilidad_q', models.CharField(max_length=50)),
                ('habilidad_e', models.CharField(max_length=50)),
                ('habilidad_c', models.CharField(max_length=50)),
                ('definitiva', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]