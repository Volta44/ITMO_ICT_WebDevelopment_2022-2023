# Generated by Django 4.1.3 on 2022-11-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='carowner',
            name='home_address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='carowner',
            name='nationality',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='carowner',
            name='passport_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
