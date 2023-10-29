# Generated by Django 4.2.5 on 2023-10-03 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_staff_notification_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
            ],
        ),
    ]