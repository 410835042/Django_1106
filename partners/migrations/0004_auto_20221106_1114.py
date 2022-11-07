# Generated by Django 3.2.9 on 2022-11-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_auto_20221106_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handsize',
            name='index_length',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='index_width',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='little_length',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='little_width',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='middle_length',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='middle_width',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='palm_length',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='palm_width',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='ring_length',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='ring_width',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='thumb_length',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='handsize',
            name='thumb_width',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
    ]