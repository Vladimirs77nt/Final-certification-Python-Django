# Generated by Django 5.0.3 on 2024-03-15 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0003_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_for_cooking',
            field=models.DurationField(),
        ),
    ]