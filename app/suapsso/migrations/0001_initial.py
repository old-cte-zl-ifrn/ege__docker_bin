# Generated by Django 2.0.6 on 2018-06-28 14:01

from django.db import migrations, models
import suapsso.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('ativo', models.BooleanField(verbose_name='Ativo')),
            ],
            options={
                'verbose_name_plural': 'Aplicações',
                'verbose_name': 'Aplicação',
            },
        ),
        migrations.CreateModel(
            name='AplicacaoProtocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(verbose_name='Ativo')),
                ('aplicacao', suapsso.models.ForeignKey(on_delete=None, to='suapsso.Aplicacao', verbose_name='Aplicação')),
            ],
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('ativo', models.BooleanField(verbose_name='Ativo')),
            ],
        ),
        migrations.AddField(
            model_name='aplicacaoprotocolo',
            name='protocolo',
            field=suapsso.models.ForeignKey(on_delete=None, to='suapsso.Protocolo', verbose_name='Protocolo'),
        ),
    ]