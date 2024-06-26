# Generated by Django 5.0.4 on 2024-05-09 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0003_alter_book_image_path_alter_book_pdf_path_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('year_of_found', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='number_of_pages',
        ),
        migrations.AddField(
            model_name='author',
            name='image_path',
            field=models.ImageField(null=True, upload_to='img/authors/'),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default='Описания нет.', max_length=300),
        ),
        migrations.AddField(
            model_name='userbooks',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notification',
            name='discard_text',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='is_accepted',
            field=models.BooleanField(null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
                ('text', models.CharField(max_length=300, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.user')),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='literary_direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.direction'),
        ),
        migrations.CreateModel(
            name='PublisherBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.book')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.user')),
            ],
        ),
    ]
