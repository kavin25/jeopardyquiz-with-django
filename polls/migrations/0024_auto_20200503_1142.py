# Generated by Django 3.0.5 on 2020-05-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_auto_20200427_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='negative_marking',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default='Null', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='pass_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]