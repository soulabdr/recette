# Generated by Django 4.1.7 on 2023-05-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_recipe_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='nbrCalories',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='nbrPersons',
            field=models.IntegerField(null=True),
        ),
    ]