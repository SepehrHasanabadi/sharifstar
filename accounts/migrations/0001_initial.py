# Generated by Django 2.2.2 on 2019-06-14 13:46

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.CharField(choices=[('stu', 'Student'), ('par', 'Parent'), ('sch', 'School'), ('opr', 'Operator')], help_text="User's type of registration.", max_length=3, verbose_name='user type')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.User')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('phone_number', models.CharField(max_length=16, verbose_name='phone number')),
                ('birth_date', models.DateTimeField(verbose_name='birth date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.User')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('operator_type', models.CharField(choices=[('act', 'accountancy')], help_text="User's type of operator.", max_length=3, verbose_name='operator type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=30, verbose_name='school name')),
                ('manager_name', models.CharField(max_length=30, verbose_name='manager name')),
                ('phone_number', models.CharField(max_length=16, verbose_name='phone number')),
                ('identity', models.IntegerField(error_messages={'unique': 'A school with that identity already exists.'}, help_text='Required. Has to be unique', unique=True, validators=[django.core.validators.RegexValidator(code='invalid_identity', message='must be a 8 digits text', regex='^\\d{8}$')], verbose_name='phone number')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User', verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('customermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.CustomerModel')),
                ('child_national_code', models.IntegerField(verbose_name='child national code')),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.customermodel',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('customermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.CustomerModel')),
                ('national_code', models.IntegerField(verbose_name='national code')),
            ],
            options={
                'permissions': [('student_discount', 'Student discount')],
            },
            bases=('accounts.customermodel',),
        ),
    ]
