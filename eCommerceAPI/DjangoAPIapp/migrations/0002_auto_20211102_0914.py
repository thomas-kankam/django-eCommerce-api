# Generated by Django 3.2.9 on 2021-11-02 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAPIapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_created']},
        ),
    ]
