# Generated by Django 4.0 on 2021-12-26 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0002_program_delete_organization_referral_referring_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='participant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='referral.participant'),
        ),
        migrations.AlterField(
            model_name='referral',
            name='referred_to_program',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='referral.program'),
        ),
        migrations.AlterField(
            model_name='referral',
            name='referring_staff',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='referral.staff'),
        ),
    ]
