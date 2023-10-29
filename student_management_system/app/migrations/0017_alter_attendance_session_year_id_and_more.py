# Generated by Django 4.2.5 on 2023-10-05 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_attendence_id_attendance_report_attendance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='session_year_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.session_year'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject'),
        ),
        migrations.AlterField(
            model_name='attendance_report',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='session_year_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.session_year'),
        ),
    ]