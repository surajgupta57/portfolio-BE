# Generated by Django 4.0.2 on 2023-06-19 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApi', '0003_reachoutform_resumeupload_testimonial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='ratings',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]