# Generated by Django 4.2.16 on 2024-09-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pic_format',
            field=models.CharField(default='jpg', max_length=10),
        ),
        migrations.AddField(
            model_name='recipe',
            name='pic_public_id',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
