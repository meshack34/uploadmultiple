# Generated by Django 4.1 on 2022-09-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_myuploadfile_delete_file_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file')),
            ],
        ),
        migrations.DeleteModel(
            name='myuploadfile',
        ),
    ]
