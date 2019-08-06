# Generated by Django 2.2.3 on 2019-07-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20190725_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image6',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tools',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]