# Generated by Django 2.2.5 on 2020-05-19 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_accomodation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyuniversity',
            name='property_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_university', to='student_accomodation.Property'),
        ),
    ]