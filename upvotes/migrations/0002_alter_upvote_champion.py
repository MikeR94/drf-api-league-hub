# Generated by Django 3.2.16 on 2022-12-28 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('champions', '0001_initial'),
        ('upvotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvote',
            name='champion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotes', to='champions.champion'),
        ),
    ]
