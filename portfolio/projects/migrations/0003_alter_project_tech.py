# Generated by Django 5.0.2 on 2024-02-28 00:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_tech'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.tech'),
        ),
    ]
