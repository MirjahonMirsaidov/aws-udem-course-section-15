# Generated by Django 5.0.2 on 2024-03-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_add_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file_path', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'FileUpload',
                'verbose_name_plural': 'FileUploads',
                'db_table': 'file',
                'ordering': ('-created_at',),
            },
        ),
    ]