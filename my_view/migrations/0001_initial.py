# Generated by Django 4.1.7 on 2023-03-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='txt_file',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('txtfile', models.FileField(upload_to='')),
            ],
        ),
    ]
