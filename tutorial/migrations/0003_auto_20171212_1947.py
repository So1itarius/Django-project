# Generated by Django 2.0 on 2017-12-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_auto_20171212_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='id',
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.TextField(max_length=50, primary_key=True, serialize=False, verbose_name='title'),
        ),
    ]
