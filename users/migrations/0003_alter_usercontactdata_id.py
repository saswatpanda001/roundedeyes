# Generated by Django 3.2.4 on 2022-04-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220419_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontactdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
