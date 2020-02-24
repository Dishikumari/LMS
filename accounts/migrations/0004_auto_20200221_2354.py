# Generated by Django 2.1.15 on 2020-02-21 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20200221_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, null=True, verbose_name='Name of Bank')),
                ('account', models.CharField(help_text='employee account number', max_length=30, null=True, verbose_name='Account Number')),
                ('branch', models.CharField(blank=True, help_text='which branch was the account issue', max_length=125, null=True, verbose_name='Branch')),
                ('salary', models.DecimalField(decimal_places=2, help_text='This is the initial salary of employee', max_digits=16, null=True, verbose_name='Starting Salary')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
                'ordering': ['-name', '-account'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('description', models.CharField(blank=True, max_length=125, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(help_text='who should we contact ?', max_length=255, null=True, verbose_name='Fullname')),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(default='+233240000000', help_text='Enter number with Country Code Eg. +233240000000', max_length=128, region=None, verbose_name='Phone Number (Example +233240000000)')),
                ('location', models.CharField(max_length=125, null=True, verbose_name='Place of Residence')),
                ('relationship', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Sister', 'Sister'), ('Brother', 'Brother'), ('Uncle', 'Uncle'), ('Aunty', 'Aunty'), ('Husband', 'Husband'), ('Wife', 'Wife'), ('Fiance', 'Fiance'), ('Cousin', 'Cousin'), ('Fiancee', 'Fiancee'), ('Niece', 'Niece'), ('Nephew', 'Nephew'), ('Son', 'Son'), ('Daughter', 'Daughter')], default='Father', help_text='Who is this person to you ?', max_length=8, null=True, verbose_name='Relationship with Person')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Emergency',
                'verbose_name_plural': 'Emergency',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Mss', 'Mss'), ('Dr', 'Dr'), ('Sir', 'Sir'), ('Madam', 'Madam')], default='Mr', max_length=4, null=True, verbose_name='Title')),
                ('image', models.FileField(blank=True, default='default.png', help_text='upload image size less than 2.0MB', null=True, upload_to='profiles', verbose_name='Profile Image')),
                ('firstname', models.CharField(max_length=125, verbose_name='Firstname')),
                ('lastname', models.CharField(max_length=125, verbose_name='Lastname')),
                ('othername', models.CharField(blank=True, max_length=125, null=True, verbose_name='Othername (optional)')),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ('Not Known', 'Not Known')], default='male', max_length=8, verbose_name='Gender')),
                ('email', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Email (optional)')),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(default='+233240000000', help_text='Enter number with Country Code Eg. +233240000000', max_length=128, region=None, verbose_name='Phone Number (Example +233240000000)')),
                ('bio', models.CharField(blank=True, default='', help_text='your biography,tell me something about yourself eg. i love working ...', max_length=255, null=True, verbose_name='Bio')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('hometown', models.CharField(blank=True, max_length=125, null=True, verbose_name='Hometown')),
                ('region', models.CharField(choices=[('Ahafo', 'Ahafo'), ('Ashanti', 'Ashanti'), ('Bono East', 'Bono East'), ('Bono', 'Bono'), ('Central', 'Central'), ('Eastern', 'Eastern'), ('Greater Accra', 'Greater Accra'), ('North East', 'Northen East'), ('Northen', 'Northen'), ('Oti', 'Oti'), ('Savannah', 'Savannah'), ('Upper East', 'Upper East'), ('Upper West', 'Upper West'), ('Volta', 'Volta'), ('Western North', 'Western North'), ('Western', 'Western')], default='Greater Accra', help_text='what region of the country(Ghana) are you from ?', max_length=20, null=True, verbose_name='Region')),
                ('residence', models.CharField(max_length=125, verbose_name='Current Residence')),
                ('address', models.CharField(blank=True, help_text='address of current residence', max_length=125, null=True, verbose_name='Address')),
                ('education', models.CharField(choices=[('Senior High', 'Senior High School'), ('Junior High', 'Junior High School'), ('Primary Level', 'Primary School'), ('Tertiary', 'Tertiary/University/Polytechnic'), ('O-LEVEL', 'OLevel'), ('Other', 'Other')], default='Senior High', help_text='highest educational standard ie. your last level of schooling', max_length=20, null=True, verbose_name='Education')),
                ('lastwork', models.CharField(blank=True, help_text='where was the last place you worked ?', max_length=125, null=True, verbose_name='Last Place of Work')),
                ('position', models.CharField(blank=True, help_text='what position where you in your last place of work ?', max_length=255, null=True, verbose_name='Position Held')),
                ('ssnitnumber', models.CharField(blank=True, max_length=30, null=True, verbose_name='SSNIT Number')),
                ('tinnumber', models.CharField(blank=True, max_length=15, null=True, verbose_name='TIN')),
                ('startdate', models.DateField(help_text='date of employement', null=True, verbose_name='Employement Date')),
                ('employeetype', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract'), ('Intern', 'Intern')], default='Full-Time', max_length=15, null=True, verbose_name='Employee Type')),
                ('employeeid', models.CharField(blank=True, max_length=10, null=True, verbose_name='Employee ID Number')),
                ('dateissued', models.DateField(help_text='date staff id was issued', null=True, verbose_name='Date Issued')),
                ('is_blocked', models.BooleanField(default=False, help_text='button to toggle employee block and unblock', verbose_name='Is Blocked')),
                ('is_deleted', models.BooleanField(default=False, help_text='button to toggle employee deleted and undelete', verbose_name='Is Deleted')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('department', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Department', verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('flag', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Nationality',
                'verbose_name_plural': 'Nationality',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced'), ('Widow', 'Widow'), ('Widower', 'Widower')], default='Single', max_length=10, null=True, verbose_name='Marital Status')),
                ('spouse', models.CharField(blank=True, max_length=255, null=True, verbose_name='Spouse (Fullname)')),
                ('occupation', models.CharField(blank=True, help_text='spouse occupation', max_length=125, null=True, verbose_name='Occupation')),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, help_text='Enter number with Country Code Eg. +233240000000', max_length=128, null=True, region=None, verbose_name='Spouse Phone Number (Example +233240000000)')),
                ('children', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Number of Children')),
                ('nextofkin', models.CharField(help_text='fullname of next of kin', max_length=255, null=True, verbose_name='Next of Kin')),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Phone Number of Next of Kin', max_length=128, null=True, region=None, verbose_name='Next of Kin Phone Number (Example +233240000000)')),
                ('relationship', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Sister', 'Sister'), ('Brother', 'Brother'), ('Uncle', 'Uncle'), ('Aunty', 'Aunty'), ('Husband', 'Husband'), ('Wife', 'Wife'), ('Fiance', 'Fiance'), ('Cousin', 'Cousin'), ('Fiancee', 'Fiancee'), ('Niece', 'Niece'), ('Nephew', 'Nephew'), ('Son', 'Son'), ('Daughter', 'Daughter')], help_text='Who is this person to you ?', max_length=15, null=True, verbose_name='Relationship with Next of Person')),
                ('father', models.CharField(blank=True, max_length=255, null=True, verbose_name="Father's Name")),
                ('foccupation', models.CharField(blank=True, max_length=125, null=True, verbose_name="Father's Occupation")),
                ('mother', models.CharField(blank=True, max_length=255, null=True, verbose_name="Mother's Name")),
                ('moccupation', models.CharField(blank=True, max_length=125, null=True, verbose_name="Mother's Occupation")),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee')),
            ],
            options={
                'verbose_name': 'Relationship',
                'verbose_name_plural': 'Relationships',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('description', models.CharField(blank=True, max_length=125, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Religion',
                'verbose_name_plural': 'Religions',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('description', models.CharField(blank=True, max_length=125, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='nationality',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Nationality', verbose_name='Nationality'),
        ),
        migrations.AddField(
            model_name='employee',
            name='religion',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Religion', verbose_name='Religion'),
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Role', verbose_name='Role'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='emergency',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee'),
        ),
        migrations.AddField(
            model_name='bank',
            name='employee',
            field=models.ForeignKey(help_text='select employee(s) to add bank account', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee'),
        ),
    ]