# Generated by Django 3.0.5 on 2020-04-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='marks_alloted',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]