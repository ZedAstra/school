# Generated by Django 2.2.12 on 2024-12-28 10:51

from django.db import migrations, models
import django.db.models.deletion
import instructor.models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0005_instructor_bio'),
        ('school', '0011_cours_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='instructeur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cours_instructeur', to='instructor.Instructor'),
            preserve_default=False,
        ),
    ]