# Generated by Django 4.0.3 on 2022-05-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITSP', '0004_alter_team_team_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Team_id',
            field=models.CharField(editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]
