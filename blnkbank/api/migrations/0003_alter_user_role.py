# Generated by Django 5.1 on 2024-08-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CUSTOMER', 'Customer'), ('LOANPROVIDER', 'Loan Provider'), ('BANKPERSONNEL', 'Bank Personnel')], default='BANKPERSONNEL', max_length=50),
        ),
    ]
