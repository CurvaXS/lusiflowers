# Generated by Django 5.0.6 on 2024-06-06 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='choise',
            field=models.CharField(choices=[('Busket', 'Busket'), ('Compositions', 'Compositions'), ('AutorsBucket', 'AutorsBucket')], max_length=100),
        ),
    ]
