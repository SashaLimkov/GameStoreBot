# Generated by Django 4.0.5 on 2022-07-03 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Тип ссылки')),
            ],
            options={
                'verbose_name': 'Тип Ссылки',
                'verbose_name_plural': 'Типы Ссылок',
            },
        ),
        migrations.AddField(
            model_name='linkgamelist',
            name='link_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.linktype', verbose_name='Тип'),
        ),
    ]