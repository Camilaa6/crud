# Generated by Django 3.0.8 on 2020-08-01 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0004_auto_20200725_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telefone',
            old_name='pertece',
            new_name='pertence',
        ),
    ]
