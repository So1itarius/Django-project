# Generated by Django 2.0 on 2017-12-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='title')),
                ('price', models.TextField(max_length=20, verbose_name='price')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100, verbose_name='full name'),
        ),
    ]
