# Generated by Django 2.2 on 2020-04-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20200419_1601'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.AddField(
            model_name='team',
            name='status',
            field=models.CharField(blank=True, choices=[('polls/images/bulls.jpg', 'Bulls'), ('polls/images/panda.jpg', 'Panda'), ('polls/images/shark.jpg', 'Shark'), ('polls/images/deer.jpg', 'Deer'), ('polls/images/wolf.jpg', 'Wolf')], default=None, max_length=2000, null=True),
        ),
    ]
