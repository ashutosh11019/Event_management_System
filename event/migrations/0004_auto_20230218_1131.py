# Generated by Django 3.1.6 on 2023-02-18 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20230218_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=3)),
                ('event_id', models.CharField(max_length=4)),
                ('booked_date', models.DateField()),
                ('participant_name', models.CharField(max_length=30)),
                ('participant_email', models.CharField(max_length=40)),
                ('participant_phone', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_status',
            field=models.CharField(choices=[('Live', 'Live'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Scheduled', 'Scheduled')], max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('Virtual', 'Virtual'), ('On-Premise', 'On-Premise')], max_length=15),
        ),
    ]
