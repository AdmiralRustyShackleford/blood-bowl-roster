# Generated by Django 4.0.5 on 2022-06-23 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('coach', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bbd.team')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=50)),
                ('skills', models.ManyToManyField(to='bbd.skill')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bbd.team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inducements', models.CharField(max_length=250)),
                ('result', models.CharField(choices=[('W', 'Win'), ('L', 'Loss'), ('D', 'Draw')], max_length=4)),
                ('opponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbd.team')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbd.season')),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbd.record'),
        ),
    ]
