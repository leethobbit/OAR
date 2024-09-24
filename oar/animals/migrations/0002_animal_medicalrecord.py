# Generated by Django 5.0.9 on 2024-09-19 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
        ('business', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('donation_fee', models.DecimalField(decimal_places=2, default=5.0, max_digits=10)),
                ('intake_date', models.DateTimeField(auto_now_add=True)),
                ('outcome_date', models.DateField(null=True)),
                ('outcome_type', models.CharField(choices=[('ADOPTION', 'Adoption'), ('DIED_IN_CARE', 'Died in Care'), ('TRANSFER', 'Transfer'), ('RETURN_TO_OWNER', 'Return to Owner')], default='ADOPTION', max_length=80)),
                ('intake_type', models.CharField(choices=[('UNKNOWN', 'Unknown'), ('OWNER_SURRENDER', 'Owner Surrender'), ('STRAY', 'Stray'), ('RETURN_TO_RESCUE', 'Return to Rescue'), ('BORN_IN_CARE', 'Born in Care')], default='OWNER_SURRENDER', max_length=80)),
                ('intake_condition', models.CharField(choices=[('UNKNOWN', 'Unknown'), ('HEALTHY', 'Healthy'), ('SICK', 'Sick'), ('INJURED', 'Injured')], default='HEALTHY', max_length=80)),
                ('current_condition', models.CharField(choices=[('UNKNOWN', 'Unknown'), ('HEALTHY', 'Healthy'), ('SICK', 'Sick'), ('INJURED', 'Injured')], default='UNKNOWN', max_length=80)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('animal_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('color', models.CharField(default='None', max_length=80)),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('starting_weight', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('ADOPTABLE', 'Adoptable'), ('QUARANTINED', 'Quarantined'), ('FOSTERED', 'Fostered'), ('MEDICAL_HOLD', 'Medical Hold'), ('ADOPTED', 'Adopted'), ('DECEASED', 'Deceased'), ('AMBASSADOR', 'Ambassador')], default='ADOPTABLE', max_length=80)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='business.location')),
                ('species', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='animals.species')),
            ],
            options={
                'db_table_comment': 'Holds information about animals',
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, default='', max_length=500)),
                ('current_weight', models.IntegerField(default=0)),
                ('bowel_movement', models.BooleanField(default=True)),
                ('treatments', models.TextField(blank=True, default='', max_length=500)),
                ('animal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='animals.animal')),
                ('q_volunteer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='people.person')),
            ],
            options={
                'db_table_comment': 'Table holds medical record entries.',
            },
        ),
    ]
