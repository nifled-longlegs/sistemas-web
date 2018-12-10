# Generated by Django 2.1.4 on 2018-12-10 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=85)),
            ],
        ),
        migrations.CreateModel(
            name='Practica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_practica', models.PositiveIntegerField()),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('archivo', models.FileField(upload_to='practicas/')),
                ('fecha', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Practica',
                'verbose_name_plural': 'Practicas',
            },
        ),
        migrations.CreateModel(
            name='PracticaAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminada', models.BooleanField(default=False)),
                ('calificacion', models.PositiveIntegerField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practicas.Alumno')),
                ('practica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practicas.Practica')),
            ],
            options={
                'verbose_name': 'Practica de Alumno',
                'verbose_name_plural': 'Practicas de Alumnos',
            },
        ),
    ]
