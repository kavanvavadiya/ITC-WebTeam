# Generated by Django 4.0.3 on 2022-05-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITSP', '0007_rename_id_team_team_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='Team_info',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='Team_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]