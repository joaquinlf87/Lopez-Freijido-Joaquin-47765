# Generated by Django 4.2.5 on 2023-10-11 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0004_contacto_remove_post_autor_remove_post_categorias_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='fecha_comentario',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='post',
        ),
    ]