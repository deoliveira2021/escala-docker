# Generated by Django 5.0.2 on 2024-03-01 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idmilitar', models.IntegerField(verbose_name='Id Militar')),
                ('idcirculo', models.IntegerField(verbose_name='Círculo')),
                ('idescala', models.IntegerField(verbose_name='Id Escala')),
                ('idsubstituto', models.IntegerField(null=True, verbose_name='Id Militar Substituto')),
                ('nomeguerra', models.CharField(max_length=40, verbose_name='Nome de Guerra')),
                ('nomesubstituto', models.CharField(blank=True, max_length=40, null=True, verbose_name='Nome de Guerra')),
                ('folga', models.IntegerField(verbose_name='Folga')),
                ('data', models.DateField(verbose_name='Data')),
                ('dia', models.CharField(max_length=15, null=True, verbose_name='Dia da Semana')),
                ('vermelha', models.BooleanField(default=False, verbose_name='Vermelha')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
                'ordering': ['data'],
            },
        ),
    ]
