# Generated by Django 5.0.6 on 2024-06-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthAssitant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='date_planted',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='disease',
            name='affected_animals',
            field=models.ManyToManyField(blank=True, to='HealthAssitant.animal'),
        ),
        migrations.AddField(
            model_name='disease',
            name='affected_crops',
            field=models.ManyToManyField(blank=True, to='HealthAssitant.crop'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
