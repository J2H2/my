# Generated by Django 2.0.1 on 2018-05-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Super staff'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='last login date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Last modified date'),
        ),
    ]
