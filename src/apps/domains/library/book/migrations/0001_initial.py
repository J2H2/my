# Generated by Django 2.0.1 on 2018-05-06 09:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('book_app', '0002_auto_20180506_1439'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('own_status', models.IntegerField(choices=[(0, 'Not own'), (1, 'Want'), (2, 'Own')], default=0, verbose_name='소유 상태')),
                ('own_date', models.DateTimeField(null=True, verbose_name='구매일')),
                ('read_status', models.IntegerField(choices=[(0, 'Not own'), (1, 'Want'), (2, 'Own')], default=0, verbose_name='읽기 상태')),
                ('read_date', models.DateTimeField(null=True, verbose_name='읽은 날')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_book_1', to='book_app.Book',
                                           verbose_name='책')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_1', to=settings.AUTH_USER_MODEL,
                                           verbose_name='유저')),
            ],
            options={
                'verbose_name': '유저 책',
                'verbose_name_plural': '유저 첵 리스트',
                'db_table': 'library_book',
            },
        ),
    ]
