# Generated by Django 3.1.14 on 2022-09-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=10, verbose_name='ユーザーネーム'),
        ),
    ]