# Generated by Django 4.2.5 on 2023-10-08 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_autor_categoria_comentario_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='avatar',
        ),
    ]
