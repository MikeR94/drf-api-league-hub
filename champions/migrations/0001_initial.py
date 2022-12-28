# Generated by Django 3.2.16 on 2022-12-28 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('champ_image', models.ImageField(default='../Ivern_0_iumwtm', upload_to='images/')),
                ('lore', models.TextField()),
                ('role', models.CharField(choices=[('top', 'Top'), ('mid', 'Mid'), ('jungle', 'Jungle'), ('adc', 'ADC'), ('support', 'Support')], default='top', max_length=32)),
                ('champ_class', models.CharField(choices=[('controller', 'Controller'), ('fighter', 'Fighter'), ('mage', 'Mage'), ('marksman', 'Marksman'), ('slayer', 'Slayer'), ('tank', 'Tank'), ('specialist', 'Specialist')], default='controller', max_length=32)),
                ('range', models.CharField(choices=[('melee', 'Melee'), ('ranged', 'Ranged')], default='melee', max_length=32)),
                ('difficulty', models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')], default='low', max_length=32)),
                ('passive_ability', models.CharField(max_length=255)),
                ('passive_ability_description', models.CharField(max_length=255)),
                ('passive_ability_image', models.ImageField(default='../IvernW_muxhxj', upload_to='images/')),
                ('ability_1', models.CharField(max_length=255)),
                ('ability_1_description', models.CharField(max_length=255)),
                ('ability_1_image', models.ImageField(default='../IvernW_muxhxj', upload_to='images/')),
                ('ability_2', models.CharField(max_length=255)),
                ('ability_2_description', models.CharField(max_length=255)),
                ('ability_2_image', models.ImageField(default='../IvernW_muxhxj', upload_to='images/')),
                ('ability_3', models.CharField(max_length=255)),
                ('ability_3_description', models.CharField(max_length=255)),
                ('ability_3_image', models.ImageField(default='../IvernW_muxhxj', upload_to='images/')),
                ('ultimate_ability', models.CharField(max_length=255)),
                ('ultimate_ability_description', models.CharField(max_length=255)),
                ('ultimate_ability_image', models.ImageField(default='../IvernW_muxhxj', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
