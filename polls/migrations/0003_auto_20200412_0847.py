# Generated by Django 3.0.5 on 2020-04-12 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_marks_alloted'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Level'),
            preserve_default=False,
        ),
    ]
