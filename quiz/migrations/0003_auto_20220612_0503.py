# Generated by Django 2.2.14 on 2022-06-12 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20220612_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='categories',
            field=models.ManyToManyField(blank=True, to='quiz.Category'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='quiz.Category'),
        ),
    ]