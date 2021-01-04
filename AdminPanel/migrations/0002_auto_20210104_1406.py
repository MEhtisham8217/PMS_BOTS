# Generated by Django 3.0.1 on 2021-01-04 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visitor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='?', max_length=1),
        ),
        migrations.CreateModel(
            name='prisoner_hospital_visits',
            fields=[
                ('prisoner_hospital_visit_id', models.AutoField(primary_key=True, serialize=False)),
                ('time_in', models.DateTimeField()),
                ('time_out', models.DateTimeField()),
                ('doctor_advise', models.CharField(max_length=200)),
                ('health_issue', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=200)),
                ('hospital', models.CharField(max_length=200)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Doctor')),
                ('jail_incharge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Jailer')),
                ('prisoner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Prisoner')),
            ],
        ),
    ]
