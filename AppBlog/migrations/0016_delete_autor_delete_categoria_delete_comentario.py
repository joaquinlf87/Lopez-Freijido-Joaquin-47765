# Generated by Django 4.2.5 on 2023-10-12 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0015_alter_comentario_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
