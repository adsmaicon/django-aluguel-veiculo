# Generated by Django 4.0.6 on 2022-07-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel_veiculos', '0003_alter_aluguel_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='valor',
            field=models.FloatField(default=0, null=True),
        ),
    ]
