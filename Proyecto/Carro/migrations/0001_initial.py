# Generated by Django 4.0.5 on 2023-07-11 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('producto_nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('costo', models.PositiveIntegerField()),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('ingresado', 'Ingresado'), ('transito', 'En transito'), ('entregado', 'Entregado')], default='ingresado', max_length=20)),
            ],
        ),
    ]