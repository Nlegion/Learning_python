# Generated by Django 3.2.6 on 2021-09-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(verbose_name='дата поступления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='provider',
            field=models.CharField(blank=True, max_length=256, verbose_name='поставщик'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.IntegerField(choices=[(1, 'шт.'), (2, 'кг.')], verbose_name='единица измерения'),
        ),
    ]