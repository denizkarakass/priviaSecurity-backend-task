# Generated by Django 4.2 on 2023-05-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_todolist_options_alter_todostep_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Yapılacaklar'),
        ),
    ]
