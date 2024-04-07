# Generated by Django 5.0.4 on 2024-04-07 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('year_of_birth', models.IntegerField()),
                ('year_of_death', models.IntegerField(null=True)),
                ('literary_direction', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_of_pages', models.IntegerField()),
                ('year_of_creating', models.IntegerField()),
                ('image_path', models.TextField()),
                ('pdf_path', models.TextField()),
                ('is_deleted', models.BooleanField()),
                ('delete_text', models.CharField(max_length=255, null=True)),
                ('is_available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon_path', models.TextField()),
                ('first_color', models.CharField(max_length=7)),
                ('second_color', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.genre'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1024)),
                ('is_accepted', models.BooleanField()),
                ('discard_text', models.CharField(max_length=1024)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.action')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('registration_date', models.DateField()),
                ('avatar_path', models.TextField(null=True)),
                ('last_book_page', models.IntegerField(null=True)),
                ('last_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='v1.book')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.role')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.user'),
        ),
        migrations.CreateModel(
            name='UserBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.user')),
            ],
        ),
    ]