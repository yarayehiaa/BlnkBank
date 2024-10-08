# Generated by Django 5.1 on 2024-08-26 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='fund_pool',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.fundpool'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='personnel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='managed_loans', to='api.bankpersonnel'),
        ),
    ]
