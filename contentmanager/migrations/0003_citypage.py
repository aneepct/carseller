# Generated by Django 2.2.1 on 2019-07-29 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contentmanager', '0002_stepone_stepthree_steptwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contents', models.TextField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentmanager.City')),
            ],
            options={
                'db_table': 'citypage_contents',
            },
        ),
    ]
