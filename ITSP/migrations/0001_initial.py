# Generated by Django 4.0.3 on 2022-05-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_name', models.CharField(max_length=50)),
                ('Team_id', models.IntegerField(default='0')),
            ],
        ),
    ]
